from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mobile(models.Model):
    brand=models.CharField(max_length=100)
    mob_name=models.CharField(max_length=100)
    price=models.IntegerField(default=10000)
    count=models.IntegerField(default=1)
    image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.mob_name

class Cart(models.Model):
    item=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("incart","incart"),
             ("cancelled","cancelled"),
             ("orderplaced","orderplaced"))
    status=models.CharField(max_length=120,choices=options,default="incart")


class Orders(models.Model):
    item=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    user=models.CharField(max_length=50)
    address=models.CharField(max_length=120)
    date_order=models.DateField(auto_now_add=True)
    options=(("orderplaced","orderplaced"),
             ("dispatch","dispatch"),
             ("intransit","intransit"),
             ("delivered","delivered"),
             ("order_cancelled","order_cancelled"))
    status=models.CharField(max_length=120,choices=options,default="orderplaced")
    expected_delivery_date=models.DateField(null=True,blank=True)


