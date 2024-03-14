from django.shortcuts import render, get_object_or_404
from .models import ChatRoom, ChatMassages
from pdf.models import PdfFile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .llm import get_vector, get_rag_promt, get_llm

# Create your views here.

@login_required
def index(request):

    chat_room = get_object_or_404(ChatRoom, user=request.user)
    files = PdfFile.objects.filter(owner = request.user)

    return render(request, 'chat/index.html', {'chat_room': chat_room, 'files':files})


@login_required
def chat_room(request):

    chat_room = get_object_or_404(ChatRoom, user=request.user)

    chat_messages = ChatMassages.objects.filter(room = chat_room)

    return render(request, 'chat/room.html', {'chatroom': chat_room, 'messages':chat_messages})


def get_chat_response(request):
    try:
        user_input = request.GET.get('message', '')

        model_response = generate_chat_response(request.user, user_input)
        return JsonResponse({'response': model_response})
    except:
        return JsonResponse({'response': "ERROR"})


def generate_chat_response(user, query):
    # files = PdfFile.objects.filter(owner = user)
    
    # vectorstore_1 = get_vector(user.username, files[0].id)
    # vectorstore_2 = get_vector(user.username, files[1].id)

    # vectorstore_1.add_texts(
    #     texts=vectorstore_2.get()['documents'],
    #     metadatas=vectorstore_2.get()['metadatas'],
    #     ids=vectorstore_2.get()['ids']
    # )
    vectorstore = get_vector(user.username)

    prompt = get_rag_promt()
    model = get_llm(vectorstore, prompt)
    result = model({"query": query})  
    return result['result']