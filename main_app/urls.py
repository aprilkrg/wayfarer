from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # City Url
    path('cities/<int:pk>', views.cities_list, name='cities'),

    # Profile Urls
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:pk>/updatephoto/', views.update_profile_photo, name='update_photo'),

    # Post Urls
    path('posts/<int:pk>', views.post_detail, name='post' ),
    path('post/<int:pk>/addpost', views.add_post, name='add_post' ),
    path('post/<int:pk>/editpost', views.edit_post, name='edit_post' ),
    path('post/<int:pk>/deletepost', views.delete_post, name='delete_post' ),
]