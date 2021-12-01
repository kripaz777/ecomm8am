from django.db import models
from home.models import *
# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 300)
	email = models.EmailField(max_length = 200)
	message = models.TextField()
	subject = models.TextField()

	def __str__(self):
		return self.name

class ContactInformation(models.Model):
	about_us = models.TextField()
	address = models.TextField()
	email = models.EmailField(max_length = 300)
	mobile_no = models.CharField(max_length = 400)
	office_no = models.CharField(max_length = 400)
	home_no = models.CharField(max_length = 400)
	logo = models.ImageField(upload_to = 'media')

	def __str__(self):
		return f"{self.email} {self.address}"