from django.contrib import admin
from .models import Event,Participants
# Register your models here.


@admin.register(Event,Participants)
class EventAdmin(admin.ModelAdmin):
    pass