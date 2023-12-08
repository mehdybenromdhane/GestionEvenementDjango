from django.urls import path
from .views import *
urlpatterns = [
    path('bonjour/<str:name>',hello  ),
    path('list/',listEvent , name="listEvent" ),

    path('listEvent/',ListEvents.as_view(),name="classListEvent"),

    path('details/<int:ide>' ,detailEvent ,name="detailEvent"),
    path('detailsClass/<int:pk>' ,Details.as_view() ,name="detailsEventClass"),

    path('add/' , addEvent , name="addEvent"),

    path('delete/<int:pk>' , deleteEvent.as_view() , name="delete"),
    path('deleteEvent/<int:ide>' , delete, name="deleteEvent"),
    path('update/<int:pk>',Update.as_view(),name="updateClass"),
    path('participer/<int:id>',participer,name="participer"),
    path('cancel/<int:id>',cancel,name="cancel"),

]
 