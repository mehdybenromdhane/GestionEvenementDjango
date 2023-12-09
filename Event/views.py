from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect

from .models import Event,Participants
from django.http import HttpResponse
from .forms import EventForm
from django.views.generic import *
# Create your views here.
from django.urls import reverse_lazy


from Person.models import Person

def hello (request , name):

    text = f"hello {name}"
    
    return render(request , 'event/list.html' , { 't':text})




def listEvent(request):

    list = Event.objects.filter(state=True).order_by('-evt_date')


    nbr_event = Event.objects.filter(state=True).count()


    return render(request , 'event/list.html', { 'list':list , 'nbr':nbr_event} )



class ListEvents(ListView):

    model=Event
    template_name="event/list.html"
    context_object_name = "list"


    def get_queryset(self):
        list = Event.objects.filter(state=True)
        return list

        











class Details(DetailView):
    model=Event
    template_name="event/details.html"
    context_object_name="event"



def detailEvent(req,ide): 

     event=  Event.objects.get(id=ide)
     user = req.user


     button =False
     participant = Participants.objects.filter(person = user, event=event)




     if participant:
         button=True
     else:
         button=False

    



     return render(req, "event/detailsEventFc.html" , {'evenement':event , 'btn':button })


def addEvent(req):

    form = EventForm()

    if req.method == 'POST':

        form = EventForm(req.POST,req.FILES)

        if form.is_valid():
         form.save()

         return redirect('listEvent')

    return render (req , "event/add.html" , {'form':form} )





class Add(CreateView):
    model= Event
    template_name = "event/add.html"
    form_class = EventForm



class Update(UpdateView):

    model= Event
    template_name = "event/update.html"
    form_class = EventForm
    success_url =  reverse_lazy('listEvent')


class deleteEvent(DeleteView):

    model=Event
    template_name= "event/delete.html"

    success_url =  reverse_lazy('listEvent')



def delete(req,ide):

    event=  Event.objects.get(id=ide)

    if event:
        event.delete()

    
    return redirect("listEvent")




def participer(req,id):

    event = Event.objects.get(id=id)
    user = Person.objects.get(cin=1144)

    if user: 
        participant = Participants.objects.create(person = user , event= event)
        participant.save()

        event.nbr_paticipants += 1

        event.save()

    return redirect("listEvent")




def cancel(req,id):

    event = Event.objects.get(id=id)
    user = Person.objects.get(cin=1144)

    if user: 
        participant = Participants.objects.filter(person = user , event= event)
        participant.delete()

        event.nbr_paticipants -= 1

        event.save()

    return redirect("listEvent")