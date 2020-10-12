from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/<int:pk>', views.cities_list, name='cities'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:pk>/updatephoto/', views.update_profile_photo, name='update_photo'),
    path('posts/<int:pk>', views.post_detail, name='post' ),
]