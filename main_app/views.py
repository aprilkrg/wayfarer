from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')


# def register(request):
#     return render( request, 'modal/modal.html' )

# def login(request):
#     return render( request, 'modal/modal.html' )