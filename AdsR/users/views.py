from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account has been created for {}. Now you can log in!".format(username))
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', context={"form":form})

@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'profile.html', context={'profile':profile})   

# @login_required
# def profile_create(request):
#     if request.user.profile.phonenumber != 1234567:
#         redirect("profile")
#     try:
#         profile = request.user.profile
#     except UserProfile.DoesNotExist:
#         profile = UserProfile(user=request.user)
    
#     else:
#         if request.method == "POST":
#             form = ProfileCreationForm(request.POST, instance=profile)
#             if form.is_valid():
#                 profile = form.save(commit=False)
#                 profile.user = request.user
#                 profile.save()
#                 redirect('home')  
#         else:
#             form = ProfileCreationForm()      
#         return render(request, 'profile_create.html', context={'form':form})