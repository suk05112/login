from django.contrib import admin
from .models import Users

# Register your models here.
#
# class user_postion(models.Model):
#      x_point = models.BigintegerFieled()
#      y_point = models.BigintegerFieled()
#
# class user_profile(models.Model):
#     id = models.CharFiedl(primary_key=True)
admin.site.register(Users)
