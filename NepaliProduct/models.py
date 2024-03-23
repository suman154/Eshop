from django.db import models

# Create your models here.
class NepaliProduct(models.Model):
    class DhakaTopi(models.Model):
        image = models.ImageField(upload_to='images/')

        
        class Daurasurwal(models.Model):
            image = models.ImageField(upload_to='images/')