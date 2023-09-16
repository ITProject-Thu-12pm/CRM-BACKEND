from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserProfile(models.Model):
    # user = models.OneToOneField(User, related_name= 'userprofile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length = 100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.AutoField(primary_key=True)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)

    # def _str_(self):
    #     return self.zip_code



     