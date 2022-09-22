from django.contrib import admin

# Register your models here.

from .models import Tournament,Participant,Pricing,Competition,Prize,Schedule,Score

admin.site.register(Tournament)
admin.site.register(Participant)
admin.site.register(Pricing)
admin.site.register(Competition)
admin.site.register(Prize)
admin.site.register(Schedule)
admin.site.register(Score)


