from django.db import models
from django.utils import timezone
# Create your models here.
class Comment(models.Model):
	name=models.CharField(max_length=20)
	comment=models.TextField()#Can be of any size
	date_added=models.DateTimeField(default=timezone.now)


	def __str__(self):
		return '<Name:{},ID:{}>'.format(self.name,self.id) #This is what is shown in the admin DB Dashboard
