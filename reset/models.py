from django.db import models

# Create your models here.
class Reset(models.Model):
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=20)
    