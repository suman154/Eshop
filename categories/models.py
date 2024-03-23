from django.db import models


# Create your models here.
class Category(models.Model):
    class WomenFashin(models.Model):
            class WomenClothing(models.Model):
                image = models.ImageField(upload_to='images/')
        

            
            class TraditionalClothing(models.Model):
                image = models.ImageField(upload_to='images/')
            
            
            
            class WomensBag(models.Model):
                image = models.ImageField(upload_to='images/')


            class WomenShoes(models.Model):
                image = models.ImageField(upload_to='images/')

            class Accessories(models.Model):
                image = models.ImageField(upload_to='images/')

            
            class LingerieSleepandLounge(models.Model):
                image = models.ImageField(upload_to='images/')



            class GirlsFashion(models.Model):
                image = models.ImageField(upload_to='images/')

            
        



    class HealthandBeauty(models.Model):
            class BathandBody(models.Model):
                image = models.ImageField(upload_to='images/')

            class BeautyTools(models.Model):
                image = models.ImageField(upload_to='images/')
        
            
            
            class Fragrances(models.Model):
                image = models.ImageField(upload_to='images/')
            
            

            class HairCare(models.Model):
                image = models.ImageField(upload_to='images/')
            
            

            class Makeup(models.Model):
                image = models.ImageField(upload_to='images/')
            
            

            class MensCare(models.Model):
                image = models.ImageField(upload_to='images/')
            

            class PersonalCare(models.Model):
                image = models.ImageField(upload_to='images/')
            
            

            class SkinCare(models.Model):
                image = models.ImageField(upload_to='images/')
            
            class FoodSupplements(models.Model):
                image = models.ImageField(upload_to='images/')

            class MedicalSupplies(models.Model):
                image = models.ImageField(upload_to='images/')





    class MensFashion(models.Model):
        class MenClothing(models.Model):
            image = models.ImageField(upload_to='images/')

        class MensBag(models.Model):
            image = models.ImageField(upload_to='images/')


        class Shoes(models.Model):
            image = models.ImageField(upload_to='images/')

                

        class BoysFashion(models.Model):
            image = models.ImageField(upload_to='images/')


        class MensUnderware(models.Model):
            image = models.ImageField(upload_to='images/')
                

            


    class WatchesandAccessories(models.Model):
        class MensWatches(models.Model):
            image = models.ImageField(upload_to='images/')

        class WomensWatches(models.Model):
            image = models.ImageField(upload_to='images/')

        class KidsWatches(models.Model):
            image = models.ImageField(upload_to='images/')

        class Sunglasses(models.Model):
            image = models.ImageField(upload_to='images/')

        class Eyeglasses(models.Model):
            image = models.ImageField(upload_to='images/')


        class WomenFashionJewellery(models.Model):
            image = models.ImageField(upload_to='images/')

        class MenFashionJewellery(models.Model):
            image = models.ImageField(upload_to='images/')
                

            
    class ElectronicDevices(models.Model):   
        class Smartphone(models.Model):
                            image = models.ImageField(upload_to='images/')

                            class FeaturePhone(models.Model):
                                image = models.ImageField(upload_to='images/')

                            class Tablets(models.Model):
                                image = models.ImageField(upload_to='images/')


                            class Desktops(models.Model):
                                image = models.ImageField(upload_to='images/')


                            class Monitors(models.Model):
                                image = models.ImageField(upload_to='images/')


                            class GamingConsole(models.Model):
                                image = models.ImageField(upload_to='images/')


                            class Cameras(models.Model):
                               image = models.ImageField(upload_to='images/')


                            class Printers(models.Model):
                                image = models.ImageField(upload_to='images/')
        
        
    class TVandHomeAppliances(models.Model):
        class Televisions(models.Model):
                                image = models.ImageField(upload_to='images/')

                                class TVAccessories(models.Model):
                                    image = models.ImageField(upload_to='images/')

                                class AudioAndVideoDevices(models.Model):
                                    image = models.ImageField(upload_to='images/')


                                class LargeAppliances(models.Model):
                                    image = models.ImageField(upload_to='images/')

                                class SmallKitchenAppliances(models.Model):
                                    image = models.ImageField(upload_to='images/')


                                clasimage = models.ImageField(upload_to='images/')

                                class VaccumsandFloorCare(models.Model):
                                    image = models.ImageField(upload_to='images/')

                                class IronandGarmentCare(models.Model):
                                    image = models.ImageField(upload_to='images/')





    class EletornicAccessories(models.Model):
        class MobileAccessories(models.Model):
                                    image = models.ImageField(upload_to='images/')

                                    class Audio(models.Model):
                                        image = models.ImageField(upload_to='images/')

                                    class Wearable(models.Model):
                                       image = models.ImageField(upload_to='images/')

                                    class ConsoleAccessories(models.Model):
                                       image = models.ImageField(upload_to='images/')

                                    class CameraAccessories(models.Model):
                                        image = models.ImageField(upload_to='images/')

                                    class ComputerAccessories(models.Model):
                                        image = models.ImageField(upload_to='images/')

                                    class Storage(models.Model):
                                        image = models.ImageField(upload_to='images/')

                                    class ComputerComponents(models.Model):
                                        image = models.ImageField(upload_to='images/')

                                    class NetworkComponents(models.Model):
                                        image = models.ImageField(upload_to='images/')



    class GroceriesandPet(models.Model):
        class Groceries(models.Model):
            image = models.ImageField(upload_to='images/')

            class Beverages(models.Model):
                image = models.ImageField(upload_to='images/')

            class BreakfastChocoandSnacks(models.Model):
                image = models.ImageField(upload_to='images/')

                    


            class FoodStaples(models.Model):
                image = models.ImageField(upload_to='images/')
                                            

            class CookingIngerdients(models.Model):
                image = models.ImageField(upload_to='images/')
                                            

            class LaundryandHousehold(models):
                image = models.ImageField(upload_to='images/')

            class WinesBeersandSpirits(models.Model):
                image = models.ImageField(upload_to='images/')
                                         


            class PetSupplies(models.Model):
                image = models.ImageField(upload_to='images/')
                                            
            class BabiesandToy(models.Model):
                class DisposableDiapers(models.Model):
                    image = models.ImageField(upload_to='images/')
                                            

        
    class HomeandLifestyle(models.Model):
        class Bath(models.Model):
            image = models.ImageField(upload_to='images/')
                                            

        class Bedding(models.Model):
            image = models.ImageField(upload_to='images/')
                                                

        class Decor(models.Model):
            image = models.ImageField(upload_to='images/')
                                            


        class Furniture(models.Model):
            image = models.ImageField(upload_to='images/')
                                                

        class KitchenandBining(models.Model):
            image = models.ImageField(upload_to='images/')
                                                

        class Lighting(models.Model):
            image = models.ImageField(upload_to='images/')
                                                


        class LaundryandCleaning(models.Model):
            image = models.ImageField(upload_to='images/')
                                                


        class ToolsDIYandOutdoor(models.Model):
            image = models.ImageField(upload_to='images/')
                                                

        class StationeryandCraft(models.Model):
            image = models.ImageField(upload_to='images/')
                                                
        class MediaMusicandBooks(models.Model):
            image = models.ImageField(upload_to='images/')
                                                

        class MusicalInstruments(models.Model):
            image = models.ImageField(upload_to='images/')
                                                

        class DigitalGoods(models.Model):
            image = models.ImageField(upload_to='images/')
                                                



        
    class SportsandOutdoor(models.Model):
        class MenShoesandClothing(models.Model):
            image = models.ImageField(upload_to='images/')

        class WomenShoesandClothing(models.Model):
            image = models.ImageField(upload_to='images/')


        class OutdoorRecreation(models.Model):
            image = models.ImageField(upload_to='images/')



        class ExerciseandFitness(models.Model):
            image = models.ImageField(upload_to='images/')

            class WaterSports(models.Model):
                image = models.ImageField(upload_to='images/')
                                                    

            class RacketSports(models.Model):
                image = models.ImageField(upload_to='images/')
                                                    


        class TeamSports(models.Model):
            image = models.ImageField(upload_to='images/')


        class WaterBottels(models.Model):
            image = models.ImageField(upload_to='images/')
                                                    
        class TravelandLuggage(models.Model):
            image = models.ImageField(upload_to='images/')
                                                    


        class SportsNutrition(models.Model):
            image = models.ImageField(upload_to='images/')
                                                    
    class MotorsToolsandDIY(models.Model):
        class Automative(models.Model):
            image = models.ImageField(upload_to='images/')
                                                   
        class Motorcycles(models.Model):
            image = models.ImageField(upload_to='images/')
                                                      

        class AutoCare(models.Model):
            image = models.ImageField(upload_to='images/')
                                                       

        class AutoEletornics(models.Model):
            image = models.ImageField(upload_to='images/')
                                                       


        class MotoPartsandAccessories(models.Model):
            image = models.ImageField(upload_to='images/')
                                                       

        class MotorcycleRidingGear(models.Model):
            image = models.ImageField(upload_to='images/')
                                                        


        class Helmets(models.Model):
            image = models.ImageField(upload_to='images/')


    class Gloves(models.Model):
        image = models.ImageField(upload_to='images/')
                                                       

    class InteriorAccessories(models.Model):
        image = models.ImageField(upload_to='images/')
                                                        

    class AutoOilsandFluids(models.Model):
        image = models.ImageField(upload_to='images/')



    class AutoTiresandWheels(models.Model):
        image = models.ImageField(upload_to='images/')
                                                       