from django.urls import path
from .views import *
urlpatterns = [
    path('bonjour/<str:name>',hello  ),
    path('list/',listEvent , name="listEvent" ),

    path('listEvent/',ListEvents.as_view(),name="classListEvent"),

    path('details/<int:ide>' ,detailsEvent ,name="detailsEvent"),
    path('detailsClass/<int:pk>' ,Details.as_view() ,name="detailsEventClass"),

    path('add/' , addEvent , name="addEvent"),

    path('delete/<int:pk>' , deleteEvent.as_view() , name="delete")
 
]
 