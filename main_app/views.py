from django.shortcuts import render
from django.http import HttpResponse

from .models import City, Post


def home( request ):
    return render(request, 'home.html')

################### NOTE City views ################################

def cities_list( request ):
    cities = City.objects.all()
    return render(request, 'city/index.html', { 'cities': cities })

####################################################################  


################### NOTE Profile views ################################

def profile(  request, pk ):
    user_post = Post.objects.filter( user_id=pk )
    return render(request, 'user/profile.html', { 'user_posts': user_post })



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

#######################################################################################

################### NOTE Post views ################################

def post_detail( request, pk ):
    post = Post.objects.get( id=pk )
    context = { 'post': post }
    return render(request, 'post/show.html', context ) 