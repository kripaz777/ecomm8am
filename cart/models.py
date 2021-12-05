from django.db import models
from home.models import Item
from django.conf import settings
# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	items = models.ForeignKey(Item,on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)
	slug = models.CharField(max_length = 300)
	checkout = models.BooleanField(default = False)

	def __str__(self):
		return self.user.username

