from django.db import models

# Create your models here.
class pricelist1(models.Model):
    gun_name = models.CharField(max_length=255)
    caliber = models.CharField(max_length=20)
    cb_price = models.CharField(max_length=7) #club member
    ncb_price = models.CharField(max_length=7) #non club member
class Caliber(models.Model): # We can add price per bullet in this model
    caliber_name = models.CharField(max_length=20)

class pricelist2(models.Model):
    gun_name = models.CharField(max_length=255)
    caliber = models.CharField(max_length=20)
    cb_price = models.DecimalField(max_digits=6, decimal_places=2) #club member
    ncb_price = models.DecimalField(max_digits=6, decimal_places=2) #non club member
    def __str__(self):
        return self.caliber_name

class pricelist3(models.Model):
    gun_name = models.CharField(max_length=255)
    caliber = models.CharField(max_length=20)
    cb_price = models.FloatField() #club member
    ncb_price = models.FloatField() #non club member
    caliber = models.ForeignKey(Caliber, on_delete=models.CASCADE)
    # We can remove prices from here and just take it from caliber
    price_cm = models.DecimalField(max_digits=6, decimal_places=2) # club member
    price_ncm = models.DecimalField(max_digits=6, decimal_places=2) # non club member

    def __str__(self):
        return self.gun_name