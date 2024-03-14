from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PdfFileForm
from .preprocess import read_pdf
from chat.llm import save_vector, get_vector
from .models import PdfFileText, PdfFile
# Create your views here.

@login_required
def upload_file(request):
    if request.method == 'POST':
        file_form = PdfFileForm( data=request.POST, files=request.FILES)
        if file_form.is_valid():
            new_file = file_form.save(commit=False)
            new_file.owner = request.user
            new_file.save()

            read_pdf(new_file)

            texts = PdfFileText.objects.filter(file__owner = request.user)
            save_vector(texts, request.user.username)
            return redirect('upload_file')
        
    file_form = PdfFileForm()
    files = PdfFile.objects.filter(owner = request.user)

    return render(request, 'pdf/upload_pdf.html', {'file_form': file_form, 'files':files})


@login_required
def delete_file(request, id):
    pdf_file = get_object_or_404(PdfFile, id = id)
        
    if pdf_file.owner == request.user:
        if request.method == 'POST':
            pdf_file.delete()
            texts = PdfFileText.objects.filter(file__owner = request.user)
            db = get_vector(request.user.username)
            db.delete_collection()
            if len(texts) != 0:
                save_vector(texts, request.user.username)
            return redirect('upload_file')
        
        return render(request, 'pdf/delete.html', {'pdf_file': pdf_file})
    else:
        return redirect('invalid')
    

@login_required
def delete_all_files(request):


    if request.method == 'POST':
        PdfFile.objects.filter(owner = request.user).delete()
      

        db = get_vector(request.user.username)
        db.delete_collection()
        
        return redirect('index')
    
    return render(request, 'pdf/delete_all.html')




