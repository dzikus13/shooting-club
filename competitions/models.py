from unicodedata import name
from django.contrib.auth import get_user_model
from django.db import models
from allauth.account.signals import user_logged_in

User = get_user_model()

def user_logged_in_receiver(request, user, **kwargs):
    print(request)
    print(user)

user_logged_in.connect(user_logged_in_receiver, sender=User)

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    def __str__(self):
        return self.name 

class Participant(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name 

class Pricing(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.price

class Competition(models.Model):
    competition_name = models.CharField(max_length=255)
    def __str__(self):
        return self.competition_name

class Prize(models.Model):
    description = models.TextField()
    place = models.DecimalField(max_digits=3, decimal_places=0)
    competition=models.ForeignKey(Competition, on_delete=models.CASCADE)
    def __str__(self):
        return self.place

class Schedule(models.Model):
    participant=models.ForeignKey(Participant, on_delete=models.CASCADE)
    competition=models.ForeignKey(Competition, on_delete=models.CASCADE)
    schedule_date = models.DateTimeField()
    def __str__(self):
        return self.participant

class Score(models.Model):
    score = models.TextField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    def __str__(self):
        return self.


