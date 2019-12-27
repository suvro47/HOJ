from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    """
    url: http://127.0.0.1:8000
    """
    return render(request, 'home.html')


def user_list(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'user_list.html', {'all_user_list': users})


def single_user(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'single_user.html', {'user': user})
