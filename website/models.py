from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=400,null=True)
    def _str_(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey( Product,null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default= 'PENDING')
    def _str_(self):
        return self.name     

