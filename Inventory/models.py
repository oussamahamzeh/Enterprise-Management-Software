from django.db import models
from datetime import datetime, timedelta


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    rebuy_till = models.IntegerField(default=0)
    purchase_cost = models.FloatField(default=0)
    shipping_cost = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)
    TVA = models.FloatField(default=0)
    code = models.CharField(max_length=256, blank=True, null=True)


    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=80)
    place = models.CharField(max_length=50)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    selling_price = models.FloatField()
    time = models.DateTimeField(blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    user =  models.CharField(max_length=100,blank=True, null=True,editable=False)
    discount = models.FloatField(default=0)
    type= models.CharField(max_length=100,editable=False)
    profit = models.FloatField()
    TVA = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        # Get the current datetime
        current_datetime = datetime.now()

        # Format the datetime as a string
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Set the formatted datetime as the value for the field
        self.time = formatted_datetime

        super().save(*args, **kwargs)

    def __str__(self):
        if self.client is not None:
            return ("%s , %s , %s, %s, %s" % (self.item.name, self.client.place, self.time, self.user, self.type))
        else:
            return ("%s , %s, %s, %s" % (self.item.name, self.time, self.user, self.type))