from django.db import models

# Create your models here.
class Banner(models.Model):
    class AddBanner(models.Model):
        formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/') 
