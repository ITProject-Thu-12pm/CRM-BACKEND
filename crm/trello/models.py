from django.db import models
from djongo import models
from user.models import User


class Column(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="column")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Card(models.Model):
    content = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='cards')


    def __str__(self):
        return self.content
