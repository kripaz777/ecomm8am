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

class SubCategoryView(BaseView):
	def get(self,request,slug):
		self.views['category'] = Category.objects.all()
		self.views['subcategory'] = SubCategory.objects.all()
		ids = SubCategory.objects.get(slug = slug).id
		self.views['subcategory'] = Item.objects.filter(subcategory_id = ids)
		return render(request,'kitchen.html',self.views)



class ItemDetailView(BaseView):
	def get(self,request,slug):
		self.views['category'] = Category.objects.all()
		self.views['subcategory'] = SubCategory.objects.all()
		self.views['item_detail'] = Item.objects.filter(slug = slug)
		return render(request,'single.html',self.views)
