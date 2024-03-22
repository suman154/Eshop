from django.db import models


# Create your models here.
class WomenFashin(models.Model):
    formats = (
        ('Clothing'),
        ('Traditional Clothing'),
        ('Womens Bag'),
        ('Shoes'),
        ('Accessories'),
        ('Lingerie, Sleep & Lounge'),
        ('Girls Fashion')
    )

class HealthandBeauty(models.Model):
    formats = (
        ('Bath & Body'),
        ('Beauty tools'),
        ('Fragrances'),
        ('Hair Care'),
        ('Makeup'),
        ('Mens Care'),
        ('Personal Care'),
        ('Skin Care'),
        ('Food Supplements'),
        ('Medical Supplies')
    )


    class MensFashion(models.Model):
        formats = (
            ('Clothing'),
            ('Mens Bag'),
            ('Shoes'),
            ('Accessories'),
            ('Boys Fashion'),
            ('Mens Underware')
        )


    class WatchesandAccessories(models.Model):
        formats = (
            ('Mens Watches'),
            ('Womens Watches'),
            ('Womens Watches'),
            ('Kids Watches'),
            ('Sunglasses'),
            ('Eyeglasses'),
            ('Women Fashion Jewellery'),
            ('Men Fashion Jewellery')

        )
    class Electronic(models.Model):
        formats = (
            ('Smartphones'),
            ('Feature Phone'),
            ('Tablets'),
            ('Laptops'),
            ('Desktops'),
            ('Monitors'),
            ('Gaming Consoles'),
            ('Camera'),
            ('Printers')

        )
    class TVandHomeAppliances(models.Model):
        formats = (
            ('Television'),
            ('TV Accessories'),
            ('Audio & Video Devices'),
            ('Large Appliance'),
            ('Small Kitchen Appliance'),
            ('Cooling & Heating'),
            ('Vaccums & Floor Care'),
            ('Iron & Garment Care'),

        )

        
    class EletornicAccessories(models.Model):
        formats = (
            ('Mobile Accessories'),
            ('Audio'),
            ('Wearable'),
            ('Console Accessories'),
            ('Camera Accessories'),
            ('Camera Accessories'),
            ('Computer Accessories'),
            ('Storage'),
            ('Computer Components'),
            ('Network Components'),
            ('Printers')

        )


    
    class GroceriesandPet(models.Model):
        formats = (
            ('Groceries'),
            ('Beverages'),
            ('Breakfast, Choco & Snacks'),
            ('Food Staples'),
            ('Cooking Ingredients'),
            ('Laundry & Household'),
            ('Wines, Beers & Spirits'),
            ('Pet Supplies')     
                        

        )


    class BabiesandToy(models.Model):
        formats = (
            ('Disposable Diapers'),
            ('Baby Gear'),
            ('Baby Personal Care'),
            ('Clothing & Accessories'),
            ('Diapering & Potty'),
            ('Feedi'),
            ('Nursery'),
            ('Baby & Toddler Toys'),
            ('Toys & Games'),
            ('Remote Control & Vehicles'),
            ('Sports & Outdoor Play'),
            ('Pacifiers & Accessories')

        )


    class HomeandLifestyle(models.Model):
        formats = (
            ('Bath'),
            ('Bedding'),
            ('Decor'),
            ('Furniture'),
            ('Kitchen & Dining'),
            ('Lighting'),
            ('Laundry & Cleaning'),
            ('Tools, DIY & Outdoor'),
            ('Stationery & Craft'),
            ('Media, Music & Books'),
            ('Musical Instruments'),
            ('Digital Goods')
        )


    class SportsandOutdoor(models.Model):
        formats = (
            ('Men Shoes & Clothing'),
            ('Women Shoes & Clothing'),
            ('Outdoor Recreation'),
            ('Exercise & Fitness'),
            ('Water Sports'),
            ('Racket Sports'),
            ('Team Sports'),
            ('Water Bottles'),
            ('Travel & Luggage'),
            ('Sports Nutrition')
        )


    class MotorsToolsandDIY(models.Model):
        formats = (
            ('Automotive'),
            ('Motorcycles'),
            ('Auto Care')
            ('Auto Electronics'),
            ('Moto Parts & Accessories'),
            ('Motorcycle Riding Gear'),
            ('Helmets'),
            ('Gloves'),
            ('Interior Accessories'),
            ('Auto Oils & Fluids'),
            ('Auto Tires & Wheels'),
            ('Lubricants')
        )