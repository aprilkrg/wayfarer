from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.TextField( max_length=255 )
    country = models.CharField( max_length=100 )

class Profile( models.Model ):
    current_city = models.CharField( max_length=100 )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )
    user_id = models.OneToOneField( User, on_delete=models.CASCADE )

class Post( models.Model ):
    title = models.CharField( max_length=100 )
    post_body = models.TextField(  max_length=255 )
    city_id = models.ForeignKey( City, on_delete=models.CASCADE, related_name="city"  )
    user_id = models.ForeignKey( User, on_delete=models.CASCADE, related_name="user" )

class Photo_profile( models.Model ):
    photo_url = models.TextField( max_length=255, default="https://www.pngitem.com/pimgs/m/294-2947257_interface-icons-user-avatar-profile-user-avatar-png.png")
    profile_id = models.OneToOneField( Profile, on_delete=models.CASCADE, related_name="profile" )   