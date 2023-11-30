
from .models import Event

from django.forms import *
class EventForm(ModelForm):
    
    class Meta:
        model = Event
        fields = "__all__"
        exclude=('state','nbr_paticipants','organisateur','participant',)
