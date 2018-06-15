from rest_framework import serializers

from .models import Language , Paradigm , Programmer

class LanguageSerializer(serializers.HyperlinkedModelSerializer):#Model Serializer shows us the relevant infomation to our model
#It also can create new models or new objects in model and also can update the object
	class Meta:
		model=Language
		fields=('id','url','name','paradigm')

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Paradigm
		fields=('id','url','name')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Programmer
		fields = ('id','url','name','languages')