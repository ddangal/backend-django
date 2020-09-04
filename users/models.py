from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.utils.timezone import now
from django.conf import settings
# Create your models here.

def upload_image_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return f'UserData/photo/{now().strftime("%Y%m%d")+filename_ext}'

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=300, blank=True, null=True)
    photo = models.FileField(upload_to=upload_image_to,blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    laititude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    direction = models.CharField(max_length=50, blank=True, null=True)
    locationkey = models.CharField(max_length=50, blank=True, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email