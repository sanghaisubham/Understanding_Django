from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer
# Create your views here.

class LanguageView(viewsets.ModelViewSet):#ModelViewSet class takes care of lot of stuff for us.Typically we have 
#to handle every single case(like Get request,POST request ,PUT or Delete).But these are all prestandard methods in
# a REST api and everyone knows what to do, and because its so consistent and probably we can use the ModelViewSet
	queryset=Language.objects.all()
	serializer_class=LanguageSerializer
