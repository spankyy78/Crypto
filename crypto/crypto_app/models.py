# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.

class Users(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default=None, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'username'


CURRENCY_CHOICES = (
    ('BTC', 'BTC'),
    ('BCH', 'BCH'),
    ('ETH', 'ETH'),
    ('ETC', 'ETC'),
    ('LTC', 'LTC'),
    ('USD', 'USD'),
    ('GBP', 'GBP'),
    ('CAD', 'CAD'),
)

ORDER_CHOICES = (
    ('UP', 'up'),
    ('DOWN', 'down')
)


class Notification(models.Model):
    user = models.ForeignKey(Users, default=None)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    order = models.CharField(max_length=4, choices=ORDER_CHOICES)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    added_at = models.TimeField(auto_created=True)

    def __str__(self):
        return '%s %s %s' % (self.currency, self.order, self.value)