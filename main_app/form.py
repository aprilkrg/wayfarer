from django import forms
from django.forms import ModelForm
from django.db.models import fields
from .models import City, Profile, Post

class CityForm( forms.ModelForm ):
    class Meta:
        model = City
        fields = ( 'name', 'image', 'country', )


class ProfileForm( forms.ModelForm ):
    class Meta:
        model = Profile
        fields = ( 'current_city', )        


class PostForm( forms.ModelForm ):
    class Meta:
        model = Post
        fields = ( 'post_body', )          