from django.urls import path

from . import views

urlpatterns = [
 path('notebook/',views.index,name='index'),     
 #Everytime notebook gets matched in the request, it will send 
 path('notebook/sign/',views.sign,name='sign')		
 #the request to views.index and the response will be returned
]

