from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from user.models import CustomUser
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            #login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Please correct the errors below!')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def profiles(request):
    users = CustomUser.objects.filter(is_superuser=False)
    return render(request, 'profiles.html', {'all_user': users})



