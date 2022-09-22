from django.shortcuts import render

# Create your views here.

from .models import Tournament

# Create your views here.

def tournament(request): # get all tournaments
    t = Tournament.objects.all()
    return render(request, "tournament/tournament.html", {"t":t})
