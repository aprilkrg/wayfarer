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
    user = models.OneToOneField( User, on_delete=models.CASCADE )

class Post( models.Model ):
    title = models.CharField( max_length=100 )
    post_body = models.TextField(  max_length=255 )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )
    city = models.ForeignKey( City, on_delete=models.CASCADE, related_name="city"  )
    user = models.ForeignKey( User, on_delete=models.CASCADE, related_name="user" )

class Photo_profile( models.Model ):
    photo_url = models.TextField( max_length=255, default="https://s3-us-west-2.amazonaws.com/adawayfarer/c4e6e5.png")
    profile = models.OneToOneField( Profile, on_delete=models.CASCADE, related_name="profile" )   