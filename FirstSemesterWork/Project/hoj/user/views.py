from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from user.models import CustomUser
from django.contrib.auth.models import User
from django.db.models import Q  # perform searching

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
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def standings(request):
    users = CustomUser.objects.filter(is_superuser=False).order_by('-problem_solved')
    # make searching
    query = request.GET.get("q")
    if query:
       users = users.filter(
           Q(username__icontains=query) |
           Q(institute__icontains=query)| 
           Q(country__icontains=query)
       )
    return render(request, 'standings.html', {'all_user': users})




