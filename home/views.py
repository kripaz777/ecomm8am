from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages

from .models import *
# Create your views here.
class BaseView(View):
	views = {}
	# views['category'] = Category.objects.all()
	# views['subcategory'] = SubCategory.objects.all()

class HomeView(BaseView):
	def get(self,request):
		# self.views['items'] = Item.objects.all()
		self.views['items'] = Item.objects.filter(stock = 'In Stock')
		self.views['ads'] = Ad.objects.all()
		self.views['sliders'] = Slider.objects.all()
		self.views['category'] = Category.objects.all()
		self.views['subcategory'] = SubCategory.objects.all()
		return render(request,'index.html',self.views)

class SubCategoryView(BaseView):
	def get(self,request,slug):
		self.views['category'] = Category.objects.all()
		self.views['subcategory'] = SubCategory.objects.all()
		ids = SubCategory.objects.get(slug = slug).id
		self.views['subcat_items'] = Item.objects.filter(subcategory_id = ids)
		return render(request,'kitchen.html',self.views)



class ItemDetailView(BaseView):
	def get(self,request,slug):
		self.views['category'] = Category.objects.all()
		self.views['subcategory'] = SubCategory.objects.all()
		self.views['item_detail'] = Item.objects.filter(slug = slug)
		self.views['sale_item'] = Item.objects.filter(labels = 'sale')

		return render(request,'single.html',self.views)


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request, 'This username is already taken.')

				return redirect('home:signup')

			elif User.objects.filter(email = email).exists():
				messages.error(request, 'This email is already taken.')

				return redirect('home:signup')

			else:

				user = User.objects.create_user(
					username = username,
					email = email,
					password = password
					)
				user.save()

				return redirect('/')

		else:
			messages.error(request, 'Password does not match.')
			return redirect('home:signup')
	return render(request,'register.html')

