from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from chat.models import ChatRoom
from .forms import RegistrationForm
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return HttpResponse("You already have account and login")
    else:
        if request.method == 'POST':
            user_form = RegistrationForm(request.POST)

            if user_form.is_valid():
                user_form.check_password()

                new_user = user_form.save(commit=False)
                data = user_form.cleaned_data

                new_user.set_password(data['password'])
                new_user.save()

                ChatRoom.objects.create(name = 'Answers bot',user=new_user)
                user = authenticate(request, username=data['username'], password=data['password'])

                login(request, user)
                return redirect('index')
        else:
            user_form = RegistrationForm()

        return render(request, 'user/register.html', {'user_form': user_form})