from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Programmer(models.Model):
	name = models.CharField(max_length=20)
	#Foreign Key means there is connection between programmer and Company table
	company = models.ForeignKey(Company,on_delete=models.CASCADE) 
	#CASCADE means if a company gets deleted,then all the programmers 
	#working for the company gets deleted too
	languages = models.ManyToManyField(Language)

	def __str__(self):
		return self.name



