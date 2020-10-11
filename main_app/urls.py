from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/', views.cities_list, name='cities'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/<int:pk>/addphoto/', views.add_profile_photo, name='add_photo'),
    path('posts/<int:pk>', views.post_detail, name='post' ),
]