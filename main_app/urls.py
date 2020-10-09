from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/', views.cities, name='cities'),
    path('register/', views.register, name='register'),
    # path('login', views.register, name='login'),
    path('profile/', views.profile, name='profile'),
]