from django.db import models

# Create your models here.
class user(models.Model):

    u_name = models.CharField(max_length=16,unique=True)

    u_password = models.CharField(max_length=32)