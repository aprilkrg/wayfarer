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
        form = UserCreationForm( request.POST )
        if form.is_valid():
            user = form.save()
            # profile = Profile.objects.create( current_city )
            profile.save()


        # login(request, user)
        # return redirect('cities')
    #   else:
    #     error_message = 'Invalid sign up - try again'
    # form = UserCreationForm()
    # context = {'form': form, 'error_message': error_message}
    # return render(request, 'auth/sign_in.html', context)


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
