from django.db import models

# Create your models here.
class SIGNUP(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=20)
    VerificationCode = models.CharField(max_length=4)
    Password = models.CharField(max_length=10)
    
    class DateofBirth(models.Model):
        Day = models.CharField()
        Month = models.CharField()
        Year = models.CharField()

