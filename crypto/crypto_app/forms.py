from django import forms
from django.forms import ModelForm

from .models import Users, Notification, ORDER_CHOICES, CURRENCY_CHOICES


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
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    order = forms.ChoiceField(choices=ORDER_CHOICES, label="", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = Notification
        fields = ['currency', 'order', 'value']

class HomeNotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['currency', 'order', 'value']