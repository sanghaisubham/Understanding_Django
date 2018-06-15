from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework import routers

#routers take care of generating all the urls for the model
router=routers.DefaultRouter() #Creates all the Default Routers
router.register('languages',views.LanguageView) #first argument is the endpoint and second argument is the view

router.register('paradigms',views.ParadigmView)

router.register('programmers',views.ProgrammerView)

#This routes are visible on http://127.0.0.1:8000/REST/    link  
urlpatterns = [
path('',include(router.urls)),

]