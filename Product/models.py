from django.db import models
from categories.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    quantity = models.DecimalField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
