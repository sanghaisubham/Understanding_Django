from django.contrib import admin

# Register your models here.
from .models import Company,Language,Programmer

admin.site.register(Company)
 #Allows to access and change the Comment models from Admin Dashboard
admin.site.register(Language)
admin.site.register(Programmer)