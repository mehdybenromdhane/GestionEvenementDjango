from django.shortcuts import render,redirect

from .models import Event
from django.http import HttpResponse
from .forms import EventForm
from django.views.generic import *
# Create your views here.
from django.urls import reverse_lazy

def hello (request , name):

    text = f"hello {name}"
    
    return render(request , 'event/list.html' , { 't':text})




def listEvent(request):

    list = Event.objects.all().order_by('-evt_date')


    nbr_event = Event.objects.count()


    return render(request , 'event/list.html', { 'list':list , 'nbr':nbr_event} )



class ListEvents(ListView):

    model=Event
    template_name="event/list.html"
    context_object_name = "list"






def detailsEvent(req , ide ):
    event = Event.objects.get(id=ide)

    c = {"event":event}

    return render (req , "event/details.html" , c)



class Details(DetailView):
    model=Event
    template_name="event/details.html"
    context_object_name="event"



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




class deleteEvent(DeleteView):

    model=Event
    template_name= "event/delete.html"

    success_url =  reverse_lazy('listEvent')



