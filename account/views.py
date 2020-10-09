from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from main_app.models import Profile
from main_app.form import ProfileForm 

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        current_city = request.POST['current_city']
        form = UserCreationForm( first_name, last_name, username, email, password, password2 )
        profile_form = ProfileForm( current_city )
        if form.is_valid():
            if profile_form.is_valid():
                user = form.save()
                profile_form.save()
                login(request, user)
                return redirect('cities')
        else:
            error_message = 'Invalid sign up - try again'
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'home.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate( username=username, password=password )
        if user is not None:
            auth.login(request, user)
            return redirect('cities')
        else:
            context = {'error':'Invalid username or password'}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('home') 
