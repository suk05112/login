from django.db import models

# Create your models here.
class Users(models.Model):
    nickname = models.CharField(max_length=200)
    account = models.CharField(max_length=200)
    profileimage = models.CharField(max_length=200)
    