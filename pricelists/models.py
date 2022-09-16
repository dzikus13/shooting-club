from django.db import models

# Create your models here.

class Caliber(models.Model): # We can add price per bullet in this model
    caliber_name = models.CharField(max_length=20)

    def __str__(self):
        return self.caliber_name

class Pricelist(models.Model):
    gun_name = models.CharField(max_length=255)
    caliber = models.ForeignKey(Caliber, on_delete=models.CASCADE)
    # We can remove prices from here and just take it from caliber
    price_cm = models.DecimalField(max_digits=6, decimal_places=2) # club member
    price_ncm = models.DecimalField(max_digits=6, decimal_places=2) # non club member
    gun_image = models.ImageField(blank=True, null=True, upload_to="guns/") # Only possible to upload images + pip install pillow

    def __str__(self):
        return self.gun_name

