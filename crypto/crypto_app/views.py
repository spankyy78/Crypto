# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')

def base(request):
    return render(request, 'base.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def signup(request):
    return render(request, 'signup.html')
# Create your views here.
