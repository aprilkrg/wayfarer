from main_app.models import Profile, Photo_profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django_email_verification import sendConfirm
# checks user and redirect them if they are valid
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail

def register(request):
    
    if request.method == 'POST':
        if request.POST is not '':
            try:
                current_city = request.POST['current_city']
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                password2 = request.POST['password2']
                if password == password2: 
                    user = User.objects.create_user( username, email, password )
                    user.save()
                    profile = Profile( current_city=current_city, user_id=user )
                    profile.save()
                    profile_photo = Photo_profile( profile_id = profile )
                    profile_photo.save()
                    user = authenticate( request, username=username, password=password )

                    if user is not None:
                        auth_login( request, user )
                        return redirect( "/profile/" )
            except:
                print('something went wrong')
                return redirect('home')

    else:
        return render( request, 'home.html' )


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password )
        if user is not None:
            auth_login(request, user)
            return redirect( "/profile/" )
        else:
            context = {'error':'Invalid username or password'}
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('home') 
