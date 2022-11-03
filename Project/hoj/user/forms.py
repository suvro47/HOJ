from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    institute = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'institute', 'country', 'password1', 'password2', )



