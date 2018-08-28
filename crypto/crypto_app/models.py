# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from coinbase.wallet.model import User

# Create your models here.

class Users(AbstractUser):
    # add additional fields in here

    description = models.TextField(max_length=255, default='')

    def __str__(self):
        return self.email