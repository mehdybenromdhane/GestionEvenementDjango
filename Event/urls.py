from django.urls import path
from .views import *
urlpatterns = [
    path('bonjour/<str:name>',hello ),
    path('list/',listEvent ),

   path('listEvent/',ListEvents.as_view() ),


]
