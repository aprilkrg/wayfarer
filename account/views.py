from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from main_app.models import Profile 

# Create your views here.

def register(request):
    error_message = ''
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('cats_index')
      else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def login( request ):
    return JsonResponse( { "login": "welcome back"} )


def logout(request):
    auth.logout(request)
    return redirect('home') 
