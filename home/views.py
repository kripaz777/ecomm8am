from django.shortcuts import render
from django.views.generic import View

from .models import *
# Create your views here.
class BaseView(View):
	views = {}
	views['category'] = Category.objects.all()
	views['subcategory'] = SubCategory.objects.all()

class HomeView(BaseView):
	def get(self,request):
		# self.views['items'] = Item.objects.all()
		self.views['items'] = Item.objects.filter(stock = 'In Stock')
		self.views['ads'] = Ad.objects.all()
		self.views['sliders'] = Slider.objects.all()

		return render(request,'index.html',self.views)