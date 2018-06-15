from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Language,Programmer,Paradigm
from .serializers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
# Create your views here.



class LanguageView(viewsets.ModelViewSet):#ModelViewSet class takes care of lot of stuff for us.Typically we have 
#to handle every single case(like Get request,POST request ,PUT or Delete).But these are all prestandard methods in
# a REST api and everyone knows what to do, and because its so consistent and probably we can use the ModelViewSet
	queryset=Language.objects.all()
	serializer_class = LanguageSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,) #Only logged  in users can have access
	#Now only logged in user can add

class ParadigmView(viewsets.ModelViewSet):#ModelViewSet class takes care of lot of stuff for us.Typically we have 
#to handle every single case(like Get request,POST request ,PUT or Delete).But these are all prestandard methods in
# a REST api and everyone knows what to do, and because its so consistent and probably we can use the ModelViewSet
	queryset=Paradigm.objects.all()
	serializer_class=ParadigmSerializer



class ProgrammerView(viewsets.ModelViewSet):#ModelViewSet class takes care of lot of stuff for us.Typically we have 
#to handle every single case(like Get request,POST request ,PUT or Delete).But these are all prestandard methods in
# a REST api and everyone knows what to do, and because its so consistent and probably we can use the ModelViewSet
	queryset=Programmer.objects.all()
	serializer_class=ProgrammerSerializer