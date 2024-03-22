from django.db import models

# Create your models here.
class Login(models.Model):
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=20)
    Password = models.CharField(max_length=10)
    
