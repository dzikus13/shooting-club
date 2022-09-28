from django.shortcuts import render
from .models import Pricelist

# Create your views here.

def pricelist(request): # get all
    pl = Pricelist.objects.all()
    return render(request, "pricelists/pricelist.html", {"pl":pl})