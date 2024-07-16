from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
   name = models.CharField( max_length=50)
   price = models.FloatField()
   category = models.CharField( max_length=50)
   description = models.CharField( max_length=150)
   quantity = models.IntegerField()
   is_active = models.BooleanField()
   image = models.ImageField(upload_to='image/')
   sid= models.ForeignKey(User, on_delete=models.CASCADE,db_column="sid")