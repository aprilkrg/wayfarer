from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField( max_length=100 )
    image = models.TextField( max_length=255 )
    country = models.CharField( max_length=100 )

class Profile(models.Model):
    user_id = models.OneToOneField( User, on_delete=models.CASCADE )
    current_city = models.CharField( max_length=100 )
    profile_photo = models.TextField( max_length=255, default="https://www.pngitem.com/pimgs/m/294-2947257_interface-icons-user-avatar-profile-user-avatar-png.png")
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )

class Post(models.Model):
    city_id = models.ForeignKey( City, on_delete=models.CASCADE, related_name="city"  )
    user_id = models.ForeignKey( User, on_delete=models.CASCADE, related_name="user" )
    post_body = models.TextField(  max_length=255 )
    title = models.CharField( max_length=100 )