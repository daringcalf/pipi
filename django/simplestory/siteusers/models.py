from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
#from django.utils.dateparse import parse_date
import datetime
#from django import forms
#from django.contrib.auth.forms import UserCreationForm

from .managers import SiteUserManager


class SiteUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(_('email address'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    #birthday = models.DateField(default=parse_date('1970-06-04'))
    birthday = models.DateField(default=datetime.date(1970, 6, 4))
    name = models.CharField(max_length=50,default='noname')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = []

    objects = SiteUserManager()

    def __str__(self):
        return f'{self.username}'
        