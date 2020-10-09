from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home( request ):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'home.html')


# def register(request):
#     return render( request, 'modal/modal.html' )

# def login(request):
#     return render( request, 'modal/modal.html' )

def cities( request ):
    return render(request, 'city/index.html') 




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