from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm 
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
    return render(request, 'profile.html')    