from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
# class CommonInfo(models.Model):
#     #  location =  models.PointField(default=None)
#      class Meta:
#         abstract = True

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user =models.IntegerField()
    bio =models.TextField(blank=True,)
    profileimg = models.ImageField(upload_to='profile_images',default='blank.jpeg')
    email= models.EmailField()

    def __str__(self) -> str:
        return self.user.username

class Houselocation(models.Model):
    name = models.CharField(max_length=100,null=True)
    maxprice=models.IntegerField() 
    minprice=models.IntegerField()
    category_name =models.ForeignKey('Category', on_delete=models.CASCADE, related_name ='Houselocation_category')
    location = models.CharField(max_length=50,null=True, ) 
     
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    HOUSE_CATEGORY = (
        ( 'Flats','Flats'),
        ( 'Apartments','Apartments'),
        ( 'Bungalow','Bungalow'),
        ( 'Offices','Offices'),
        ( 'Studentresidence','Studentresidence'),
        ( 'Bedsitters','Bedsitters'),
        ( 'Singleroom','Singleroom'),
    )
    
    categoryname= models.CharField(max_length=20, choices=HOUSE_CATEGORY,null=True)
    bathroom=models.CharField(max_length=50,null=True)
    kitchen=models.CharField(max_length=50,null=True)
    bedroom=models.CharField(max_length=50,null=True)
   
 
    



    