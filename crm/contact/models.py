from django.db import models
from userprofile.models import UserProfile


# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)

    # To retrieve contacts for a specific user, filter the contacts collection by the user's identifier.
    belong_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # the user_profile field will be NULL for contacts who aren't users. For contacts who are also users, 
    # this field will contain a reference to their UserProfile

    # user_profile = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length = 100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.contact_id