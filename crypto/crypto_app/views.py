# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from crypto_app.forms import UserForm, NotificationForm, LoginForm


class UsersFormView(View):
    form_class = UserForm
    template = 'signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, { 'form': form })

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
                return redirect('home')

        return render(request, 'home.html',)

class NotificationFormView(View):
    form_class = NotificationForm
    template = 'notification.html'

    @login_required(login_url="/accounts/login")
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, { 'form': form })

    @login_required(login_url="/accounts/login")
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.added_at = datetime.now()
            notification.save()

        return render(request, 'notification.html')

    #@login_required(login_url="/accounts/login")
    #def put(self, request):

    #@login_required(login_url="/accounts/login")
    #def delete(self, request):

def connect(request):
    form = LoginForm

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')

    return render(request, 'registration/login.html', {'form': form })

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'signup.html')


