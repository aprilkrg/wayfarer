from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
# from .models import Profile

# Create your views here.

def register( request ):
    return JsonResponse( { "register": "new user"} )

def login( request ):
    return JsonResponse( { "login": "welcome back"} )


def logout(request):
    auth.logout(request)
    return redirect('home') 
