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

				return redirect('/accounts/login')

		else:
			messages.error(request, 'Password does not match.')
			return redirect('home:signup')
	return render(request,'register.html')


class Search(BaseView):
	def get(self,request):
		if request.method == 'GET':

			query = request.GET['query']
			if query is None:
				return redirect('/')
			self.views['search_product'] = Item.objects.filter(name__icontains = query)
		return render(request,'search.html',self.views)


		# -----------------------API----------------------
from django.urls import path, include
from .models import Item
from rest_framework import routers, serializers, viewsets
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category', 'subcategory','status','stock','labels']
    search_fields = ['name','description']
    ordering_fields = ['id','name','price','discounted_price']



class ItemCRUDView(APIView):
	def get_object(self,pk):
		try:
			return Item.objects.get(pk = pk)
		except:
			pass

	def get(self,request,pk,format = None):
		item = self.get_object(pk)
		serializer = ItemSerializer(item)
		return Response(serializer.data)

	def put(self,request,pk,format = None):
		item = self.get_object(pk)
		serializers = ItemSerializer(item,data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data)
		return Response("There is an Error", status = status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format = None):
		item = self.get_object(pk)
		item.delete()
		return Response("Data is removed or deleted!",status = status.HTTP_200_OK)
