from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

import uuid
import boto3
from .models import City, Post, Photo_profile, Profile

# Add these "constants" below the imports
S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'adawayfarer'

################### NOTE Landing / About page #######################

def home( request ):
    return render(request, 'home.html' )

####################################################################
    

################### NOTE City views ################################

def cities_list( request,  pk=1 ):
    # user = User.objects.get(id=request.user.id)
    print(request.user.profile.__dict__)
    cities = City.objects.all()
    city = City.objects.get(id=pk)
    posts = Post.objects.filter(city=pk)

    context = {
        'cities': cities,
        'city': city,
        'posts': posts.order_by('-created_at')
    }

    return render(request, 'city/index.html', context )

####################################################################  


################### NOTE Profile views ################################


def profile(  request ):
    user_post = Post.objects.filter( user=request.user.id )
    profile_photo = Photo_profile.objects.get( profile=request.user.id )

    context = {
        'user_posts': user_post,
        'profile_photo': profile_photo.photo_url,
    }

    return render(request, 'user/profile.html', context )



def update_profile_photo( request, pk ):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get( 'photo-file', None )
    print( 'photo_file:', photo_file)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        print('s3:', s3, 'key:', key )
        # just in case something goes wrong
        try:
            s3.upload_fileobj( photo_file, BUCKET, key )
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            print(url)
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo_profile.objects.get( profile=pk )
            photo.photo_url = url
            photo.save()
            redirect("/profile")

        except:
            print('An error occurred uploading file to S3')
    return redirect("/profile/")


# todo : error handling
def profile_edit(request, pk):
    if request.method == 'POST':
        current_city = request.POST['current_city']
        print(current_city)
        # overwrite the value of current city (den) to input value (chicago)
        # user.profile.current_city = current_city
        user = User.objects.get(id=pk)
        profile = Profile.objects.get(id=pk)
        user.username = request.POST['username']
        user.save()
        print(user.username, 'User name <<<<')
        profile.current_city = request.POST['current_city']
        profile.save()
        print(current_city, 'current city <<<<')
        return redirect("/profile/")
    else:
        return render(request, 'user/profile_edit.html')  

#####################################################################

################### NOTE Post views ################################

def post_detail( request, pk ):
    post = Post.objects.get( id=pk )
    context = { 'post': post }
    return render(request, 'post/show.html', context ) 


def add_post( request, pk ):

    current_city = pk
    if request.method == 'POST':
        if request.POST != '':
            try:
                title = request.POST['title']
                body = request.POST['post_body']
                city = City.objects.get( id=request.POST['city_id'] )
                user = User.objects.get( id=request.user.id ) 
                new_post = Post( title=title,  post_body=body, city=city, user=user )
                new_post.save()
                return redirect(f'/cities/{ current_city }')
            except:
                print('Something went wrong')
                error = 'form can not be empty'
                context = {
                    'error': error,
                }
                return redirect(f'/cities/{ current_city }')
                # return render( request, 'city/index.html', context )
    

def delete_post ( request, pk ):
    Post.objects.get( id=pk ).delete()
    return redirect('cities')