from django.shortcuts import render
from .models import Tournament
# Create your views here.


def tournament(request): # get all tournaments
    t = Tournament.objects.all()
    return render(request, "tournament.html", {"t":t})

from .models import Tournament

# Create your views here.

def tournament(request): # get all tournaments
    t = Tournament.objects.all()
    return render(request, "tournament/tournament.html", {"t":t})

