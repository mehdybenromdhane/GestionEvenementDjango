from django.shortcuts import render

from .models import Event
from django.http import HttpResponse

from django.views.generic import ListView
# Create your views here.


def hello (request , name):

    text = f"hello {name}"
    
    return render(request , 'event/list.html' , { 't':text})




def listEvent(request):

    list = Event.objects.all()


    return render(request , 'event/list.html', { 'list':list} )



class ListEvents(ListView):

    model=Event
    template_name="event/list.html"
    context_object_name = "list"




