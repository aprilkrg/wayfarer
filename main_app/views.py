from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create your views here.

def home( request ):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')


def register(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cities')
        else:
            error_message = 'Invalid register, try again'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message,
    }
    return render( request, 'modal/modal.html', context )

# def login(request):
#     return render( request, 'modal/modal.html' )

def cities( request ):
    return HttpResponse('<h1>Cities</h1>') 