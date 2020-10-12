from django.contrib import admin
from .models import City, Profile, Post, Photo_profile 

# Register your models here.
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Photo_profile)
admin.site.register(Post)