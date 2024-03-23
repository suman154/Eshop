from django.db import models


# Create your models here.
class WomenFashin(models.Model):
        class Clothing(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/') 

        
        class TraditionalClothing(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        
        
        class WomensBag(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')


        class Shoes(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')


        class Accessories(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')


        
        class LingerieSleepandLounge(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')



        class GirlsFashion(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')

        
    







class HealthandBeauty(models.Model):
        class BathandBody(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
   

        class BeautyTools(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
    
        
        
        class Fragrances(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        

        class HairCare(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        

        class Makeup(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        

        class MensCare(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        

        class PersonalCare(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        

        class SkinCare(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        
        class FoodSupplements(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        
        class MedicalSupplies(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
        file_format = models.CharField(max_length=4, choices=format)
        image = models.ImageField(upload_to='images/')
        





class MensFashion(models.Model):
       class Clothing(models.Model):
                formats = (
                ('JPEG', 'JPEG'),
                ('PNG', 'PNG'),
                ('GIF', 'GIF'),
                ('SVG', 'SVG'),
                )
     
                file_format = models.CharField(max_length=4, choices=format)
                image = models.ImageField(upload_to='images/')


                class MensBag(models.Model):
                    formats = (
                    ('JPEG', 'JPEG'),
                    ('PNG', 'PNG'),
                    ('GIF', 'GIF'),
                    ('SVG', 'SVG'),
                    )
     
                file_format = models.CharField(max_length=4, choices=format)
                image = models.ImageField(upload_to='images/')


                class Shoes(models.Model):
                    formats = (
                    ('JPEG', 'JPEG'),
                    ('PNG', 'PNG'),
                    ('GIF', 'GIF'),
                    ('SVG', 'SVG'),
                )
     
                file_format = models.CharField(max_length=4, choices=format)
                image = models.ImageField(upload_to='images/')


                class Accessories(models.Model):
                    formats = (
                    ('JPEG', 'JPEG'),
                    ('PNG', 'PNG'),
                    ('GIF', 'GIF'),
                    ('SVG', 'SVG'),
                )
     
                file_format = models.CharField(max_length=4, choices=format)
                image = models.ImageField(upload_to='images/')
            

                class BoysFashion(models.Model):
                    formats = (
                    ('JPEG', 'JPEG'),
                    ('PNG', 'PNG'),
                    ('GIF', 'GIF'),
                    ('SVG', 'SVG'),
                )
     
                file_format = models.CharField(max_length=4, choices=format)
                image = models.ImageField(upload_to='images/')


                class MensUnderware(models.Model):
                    formats = (
                    ('JPEG', 'JPEG'),
                    ('PNG', 'PNG'),
                    ('GIF', 'GIF'),
                    ('SVG', 'SVG'),
                )
     
                file_format = models.CharField(max_length=4, choices=format)
                image = models.ImageField(upload_to='images/')
            
            

        


class WatchesandAccessories(models.Model):
       class MensWatches(models.Model):
                    formats = (
                    ('JPEG', 'JPEG'),
                    ('PNG', 'PNG'),
                    ('GIF', 'GIF'),
                    ('SVG', 'SVG'),
                )
     
                    file_format = models.CharField(max_length=4, choices=format)
                    image = models.ImageField(upload_to='images/')


                    class WomensWatches(models.Model):
                        formats = (
                        ('JPEG', 'JPEG'),
                        ('PNG', 'PNG'),
                        ('GIF', 'GIF'),
                        ('SVG', 'SVG'),
                    )
     
                    file_format = models.CharField(max_length=4, choices=format)
                    image = models.ImageField(upload_to='images/')


                    class KidsWatches(models.Model):
                        formats = (
                        ('JPEG', 'JPEG'),
                        ('PNG', 'PNG'),
                        ('GIF', 'GIF'),
                        ('SVG', 'SVG'),
                    )
     
                    file_format = models.CharField(max_length=4, choices=format)
                    image = models.ImageField(upload_to='images/')


                    class Sunglasses(models.Model):
                        formats = (
                        ('JPEG', 'JPEG'),
                        ('PNG', 'PNG'),
                        ('GIF', 'GIF'),
                        ('SVG', 'SVG'),
                    )
     
                    file_format = models.CharField(max_length=4, choices=format)
                    image = models.ImageField(upload_to='images/')


                    class Eyeglasses(models.Model):
                        formats = (
                        ('JPEG', 'JPEG'),
                        ('PNG', 'PNG'),
                        ('GIF', 'GIF'),
                        ('SVG', 'SVG'),
                    )
     
                    file_format = models.CharField(max_length=4, choices=format)
                    image = models.ImageField(upload_to='images/')


                    class WomenFashionJewellery(models.Model):
                        formats = (
                        ('JPEG', 'JPEG'),
                        ('PNG', 'PNG'),
                        ('GIF', 'GIF'),
                        ('SVG', 'SVG'),
                    )
     
                    file_format = models.CharField(max_length=4, choices=format)
                    image = models.ImageField(upload_to='images/')


                    class MenFashionJewellery(models.Model):
                        formats = (
                        ('JPEG', 'JPEG'),
                        ('PNG', 'PNG'),
                        ('GIF', 'GIF'),
                        ('SVG', 'SVG'),
                    )
     
                    file_format = models.CharField(max_length=4, choices=format)
                    image = models.ImageField(upload_to='images/')
                
            

        
class ElectronicDevices(models.Model):   
       class Smartphone(models.Model):
                        formats = (
                        ('JPEG', 'JPEG'),
                        ('PNG', 'PNG'),
                        ('GIF', 'GIF'),
                        ('SVG', 'SVG'),
                    )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')


                        class FeaturePhone(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                        )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')


                        class Tablets(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                        )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')


                        class Desktops(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                        )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')


                        class Monitors(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                        )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')


                        class GamingConsole(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                        )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')


                        class Cameras(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                        )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')


                        class Printers(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                        )
     
                        file_format = models.CharField(max_length=4, choices=format)
                        image = models.ImageField(upload_to='images/')
       
       
       
       
class TVandHomeAppliances(models.Model):
       class Televisions(models.Model):
                            formats = (
                            ('JPEG', 'JPEG'),
                            ('PNG', 'PNG'),
                            ('GIF', 'GIF'),
                            ('SVG', 'SVG'),
                            )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')


                            class TVAccessories(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')


                            class AudioAndVideoDevices(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')


                            class LargeAppliances(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')


                            class SmallKitchenAppliances(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')


                            class CoolingandHeating(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')


                            class VaccumsandFloorCare(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')


                            class IronandGarmentCare(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                            file_format = models.CharField(max_length=4, choices=format)
                            image = models.ImageField(upload_to='images/')





class EletornicAccessories(models.Model):
       class MobileAccessories(models.Model):
                                formats = (
                                ('JPEG', 'JPEG'),
                                ('PNG', 'PNG'),
                                ('GIF', 'GIF'),
                                ('SVG', 'SVG'),
                                )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class Audio(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class Wearable(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class ConsoleAccessories(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class CameraAccessories(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class ComputerAccessories(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class Storage(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class ComputerComponents(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class NetworkComponents(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')


                                class Printers(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                file_format = models.CharField(max_length=4, choices=format)
                                image = models.ImageField(upload_to='images/')





class GroceriesandPet(models.Model):
      class Groceries(models.Model):
                                    formats = (
                                    ('JPEG', 'JPEG'),
                                    ('PNG', 'PNG'),
                                    ('GIF', 'GIF'),
                                    ('SVG', 'SVG'),
                                    )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')


                                    class Beverages(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')


                                    class BreakfastChocoandSnacks(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')


                                    class FoodStaples(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')


                                    class CookingIngerdients(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')


                                    class LaundryandHousehold(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')


                                    class WinesBeersandSpirits(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')


                                    class PetSupplies(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),3
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
     
                                    file_format = models.CharField(max_length=4, choices=format)
                                    image = models.ImageField(upload_to='images/')



class BabiesandToy(models.Model):
       class DisposableDiapers(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')



       
class HomeandLifestyle(models.Model):
       class Bath(models.Model):
                                        formats = (
                                        ('JPEG', 'JPEG'),
                                        ('PNG', 'PNG'),
                                        ('GIF', 'GIF'),
                                        ('SVG', 'SVG'),
                                        )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class Bedding(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class Decor(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class Furniture(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class KitchenandBining(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class Lighting(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class LaundryandCleaning(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class ToolsDIYandOutdoor(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class StationeryandCraft(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class MediaMusicandBooks(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class MusicalInstruments(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


                                        class DigitalGoods(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                        file_format = models.CharField(max_length=4, choices=format)
                                        image = models.ImageField(upload_to='images/')


       
class SportsandOutdoor(models.Model):
       class MenShoesandClothing(models.Model):
                                            formats = (
                                            ('JPEG', 'JPEG'),
                                            ('PNG', 'PNG'),
                                            ('GIF', 'GIF'),
                                            ('SVG', 'SVG'),
                                            )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')


                                            class WomenShoesandClothing(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')


                                            class OutdoorRecreation(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')



                                            class ExerciseandFitness(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')



                                            class WaterSports(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')



                                            class RacketSports(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')



                                            class TeamSports(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')



                                            class WaterBottels(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')



                                            class TravelandLuggage(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')



                                            class SportsNutrition(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
        
                                            file_format = models.CharField(max_length=4, choices=format)
                                            image = models.ImageField(upload_to='images/')

class MotorsToolsandDIY(models.Model):
       class Automative(models.Model):
                                                formats = (
                                                ('JPEG', 'JPEG'),
                                                ('PNG', 'PNG'),
                                                ('GIF', 'GIF'),
                                                ('SVG', 'SVG'),
                                                )
            
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')


                                                class Motorcycles(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
            
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')


                                                class AutoCare(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')


                                                class AutoEletornics(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')


                                                class AutoCare(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')


                                                class MotoPartsandAccessories(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')



                                                class MotorcycleRidingGear(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')



                                                class Helmets(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')



                                                class Gloves(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')



                                                class InteriorAccessories(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')



                                                class AutoOilsandFluids(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')



                                                class AutoTiresandWheels(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')


                                                
                                                class Lubricants(models.Model):
                                                    formats = (
                                                    ('JPEG', 'JPEG'),
                                                    ('PNG', 'PNG'),
                                                    ('GIF', 'GIF'),
                                                    ('SVG', 'SVG'),
                                                    )
        
                                                file_format = models.CharField(max_length=4, choices=format)
                                                image = models.ImageField(upload_to='images/')


                                                