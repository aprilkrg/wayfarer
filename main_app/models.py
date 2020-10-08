from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField( max_length=100 )
    image = models.TextField()
    country = models.CharField( max_length=100 )

class Profile(models.Model):
    user_id = models.OneToOneField( User, on_delete=models.CASCADE )
    current_city = models.OneToOneField( City, on_delete=models.CASCADE )
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )

class Post(models.Model):
    city_id = models.OneToOneField( City, on_delete=models.CASCADE, related_name="city"  )
    user_id = models.OneToOneField( User, on_delete=models.CASCADE, related_name="user" )