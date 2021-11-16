from django.db import models

# Create your models here.

LABELS = (('new','new'),('sale','sale'),('hot','hot'),('','default'))
STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
STATUS = (('active','active'),('','Not active'))
class Category(models.Model):
	name = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media',null = True)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media',null = True)

	def __str__(self):
		return self.name 


class Item(models.Model):
	name = models.TextField()
	slug = models.CharField(max_length = 500, unique = True)
	price = models.IntegerField()
	discounted_price = models.IntegerField(default = 0)
	image = models.ImageField(upload_to = 'media',null = True)
	description = models.TextField(blank = True)
	labels = models.CharField(choices = LABELS,max_length = 100,blank = True)
	status = models.CharField(choices = STATUS,max_length = 100,blank = True)
	stock = models.CharField(choices = STOCK,max_length = 100,blank = True)

	def __str__(self):
		return self.name 