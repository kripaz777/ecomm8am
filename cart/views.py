from django.shortcuts import render
from .models import *
from home.models import Item
from home.views import *
from django.urls import reverse

from django.contrib.auth.decorators import login_required
# Create your views here.
class CartView(BaseView):
	def get(self,request):
		self.views['view_cart'] = Cart.objects.filter(user = request.user,checkout = False)
		return render(request,'cart.html',self.views)

@login_required
def cart(request,slug):
	if Item.objects.filter(stock = 'In Stock'):
		if Cart.objects.filter(slug = slug).exists():
			quantity = Cart.objects.get(slug = slug).quantity
			quantity = quantity +1
			price = Item.objects.get(slug = slug).price
			discounted_price = Item.objects.get(slug = slug).discounted_price
			if discounted_price > 0:
				original_price = discounted_price
			else:
				original_price = price
			subtotal = quantity*original_price
			Cart.objects.filter(slug = slug).update(quantity = quantity,sub_total = subtotal)
		else:
			price = Item.objects.get(slug = slug).price
			discounted_price = Item.objects.get(slug = slug).discounted_price
			if discounted_price > 0:
				original_price = discounted_price
			else:
				original_price = price
			username = request.user
			subtotal = original_price
			data = Cart.objects.create(
				user = username,
				slug = slug,
				items = Item.objects.filter(slug = slug)[0],
				sub_total = subtotal
				)
			data.save()
	else:
		messages.error(request, 'This item is out of stock')
		return redirect('/')

	return redirect('/cart')

def remove_cart(request,slug):
	if Cart.objects.filter(slug = slug).exists():
		quantity = Cart.objects.get(slug = slug).quantity
		price = Item.objects.get(slug = slug).price
		discounted_price = Item.objects.get(slug = slug).discounted_price
		if discounted_price > 0:
			original_price = discounted_price
		else:
			original_price = price

		
		if quantity >1:
			quantity = quantity - 1
			subtotal = original_price*quantity
			Cart.objects.filter(slug = slug).update(quantity = quantity,sub_total = subtotal)
			messages.success(request, 'The quantity is decreased.')
			return redirect('cart:cart')
		else:
			return redirect('cart:cart')
		
	else:
		messages.error(request, 'Thie product is not in our list.')
		return redirect('/')

def delete_cart(request,slug):
	if Cart.objects.filter(slug = slug).exists():
		Cart.objects.filter(slug = slug).delete()
		messages.success(request, 'The cart is deleted.')
		return redirect('cart:cart')

	else:
		messages.success(request, 'The cart is deleted.')
		return redirect('cart:cart')