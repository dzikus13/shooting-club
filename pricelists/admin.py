from django.contrib import admin

# Register your models here.

from .models import Pricelist, Caliber

admin.site.register(Pricelist)
admin.site.register(Caliber)