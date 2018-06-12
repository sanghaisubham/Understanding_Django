from rest_framework import serializers

from .models import Language

class LanguageSerializer(serializers.ModelSerializer):#Model Serializer shows us the relevant infomation to our model
#It also can create new models or new objects in model and also can update the object
	class Meta:
		model=Language
		fields=('id','name','paradigm')