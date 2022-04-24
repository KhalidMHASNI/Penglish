from distutils.command.upload import upload
from math import fabs
from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class User():
    pass