from main_app.models import Profile
from main_app.views import profile
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from main_app.form import ProfileForm 

def register(request):
    print(request.method, '/register' )

    if request.method == 'POST':
        current_city = request.POST['current_city']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2: 
            user = User.objects.create_user( username, email, password )
            user.save()
            profile = Profile(current_city=current_city, user_id=user )
            profile.save()
            # return redirect( 'profile' )
            user = authenticate( request, username=username, password=password )
            
            if user is not None:
                login( request, user )
                return redirect( 'profile' )
        else:
            return render( request, 'home.html' )


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
