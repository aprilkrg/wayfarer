from django.shortcuts import render, redirect

import uuid
import boto3
from .models import City, Post, Photo_profile

# Add these "constants" below the imports
S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'adawayfarer'

################### NOTE Landing / About page #######################

def home( request ):
    return render(request, 'home.html' )

####################################################################
    

################### NOTE City views ################################

def cities_list( request ):
    cities = City.objects.all()
    return render(request, 'city/index.html', { 'cities': cities })

####################################################################  


################### NOTE Profile views ################################

def profile(  request, pk ):
    user_post = Post.objects.filter( user_id=pk )
    profile_photo = Photo_profile.objects.get( profile_id=pk )

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
            photo = Photo_profile.objects.get( profile_id=pk )
            photo.photo_url = url
            photo.save()
            redirect(f"/profile/{ pk }")

        except:
            print('An error occurred uploading file to S3')
    return redirect(f"/profile/{ pk }")



# def profile_edit(request):
#     user = request.user
#     if request.method == 'POST':
#         try:
#             profile_form = Profile_Form(request.POST, request.FILES, instance=user.profile)
#             if profile_form.is_valid():
#                 new_profile = profile_form.save(commit=False)
#                 new_profile.user = request.user
#                 profile.image = request.FILES['image']
#                 new_profile.save()
#         except:
#             profile_form = Profile_Form(request.POST, request.FILES)
#             if profile_form.is_valid():
#                 new_profile = profile_form.save(commit=False)
#                 new_profile.user = request.user
#                 profile.image = request.FILES['image']
#                 new_profile.save()
#         return redirect('profile')
#     else:
#         try:
#             profile_form = Profile_Form(instance=user.profile)
#             context = {'profile_form': profile_form}
#             return render(request, 'account/edit.html', context)
#         except:
#             profile_form = Profile_Form()
#             context = {'profile_form': profile_form}
#             return render(request, 'account/edit.html', context)    

#####################################################################

################### NOTE Post views ################################

def post_detail( request, pk ):
    post = Post.objects.get( id=pk )
    context = { 'post': post }
    return render(request, 'post/show.html', context ) 