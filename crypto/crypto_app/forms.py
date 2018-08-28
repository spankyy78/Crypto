from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users

from django.contrib.auth import get_user_model
Users = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Users
        fields = ('username', 'email')