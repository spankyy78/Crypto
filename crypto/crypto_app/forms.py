from django import forms
from django.forms import ModelForm

from .models import Users, Notification


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['username', 'password']

class NotificationForm(ModelForm):
    currency = forms.ChoiceField()
    order = forms.ChoiceField()

    class Meta:
        model = Notification
        fields = ['currency', 'order', 'value']