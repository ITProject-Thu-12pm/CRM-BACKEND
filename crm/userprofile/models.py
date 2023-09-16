from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    # user = models.OneToOneField(User, related_name= 'userprofile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=8)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


     