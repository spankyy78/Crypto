# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from crypto_app.forms import UserForm, NotificationForm, LoginForm
from crypto_app.models import Notification


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

class NotificationFormView(LoginRequiredMixin, View):
    form_class = NotificationForm
    template = 'notification.html'


    def get(self, request):
        notifications = Notification.objects.all()
        form = self.form_class(None)
        return render(request, self.template, {'form': form}, {'notifications': notifications})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.user = request.user
            notification.added_at = datetime.now()
            notification.save()

        return redirect('home')

    def put(self, request, pk):
        notification = self.get_object(pk)
        form = self.form_class(request.POST)
        if notification.is_valid():
            notification.save()

        return redirect('home')

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

    return render(request, 'registration/login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'signup.html')


