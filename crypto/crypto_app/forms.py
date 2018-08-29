from django import forms
from django.forms import ModelForm

from .models import Users

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
