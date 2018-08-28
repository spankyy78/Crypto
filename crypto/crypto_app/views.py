# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Users

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')

def base(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'signup.html')
# Create your views here.
