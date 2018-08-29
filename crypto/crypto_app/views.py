# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from crypto_app.forms import UserForm


class UsersFormView(View):
    form_class = UserForm
    template = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, email=email, password=password)

            if user is not None and user.is_active:
                login(request, user)
                redirect('home.html')

        return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'signup.html')
