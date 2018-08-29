from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Users

from django.contrib.auth import get_user_model
#Users = get_user_model()

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'email', 'password']

#class CustomUserCreationForm(UserCreationForm):
#
#   class Meta(UserCreationForm.Meta):
#       model = Users
#       fields = ('username', 'email')
#
#class CustomUserChangeForm(UserChangeForm):
#
#    class Meta:
#        model = Users
#        fields = ('username', 'email')