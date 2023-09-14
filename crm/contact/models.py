from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def _str_(self):
        return self.contact_id