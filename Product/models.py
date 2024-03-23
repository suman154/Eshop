from django.db import models
from categories.models import categories

# Create your models here.
class Product(models.Models):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    quantity = models.DecimalField()
    category = models.ForeignKey(categories,on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=255, Blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
