from django.contrib import admin
from .models import Event,Participants

from datetime import datetime
class nbr_Participation(admin.SimpleListFilter):
    title = 'Number of participations'
    parameter_name = 'nbr_paticipants'

    def lookups(self, request, model_admin):
        return (
            ('No', ("No participants")),
            ('Yes', ("There are participants ")),
            
        )

    def queryset(self, request, queryset):
        if self.value() == 'No':
            return queryset.filter(nbr_paticipants__exact=0)
        if self.value() == 'Yes':
            return queryset.filter(nbr_paticipants__gt=0)
        



       
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    
     list_display=('title','category','evt_date','state','nbr_paticipants' ,'created_at')

     readonly_fields=('created_at','updated_at',)

     def numberOfParticipants(self,obj):
          nb = obj.participant.count()
          return nb
     list_per_page = 2

     list_filter=('title',nbr_Participation,)

@admin.register(Participants)
class participationAdmin(admin.ModelAdmin):
    pass