from django.shortcuts import render
from .models import *
from home.models import Item
from home.views import *
from django.contrib.auth.decorators import login_required
# Create your views here.
class CartView(BaseView):
	def get(request):
		self.views['view_cart'] = Cart.objects.filter(user = request.user,checkout = False)
		return render(request,'cart.html',self.views)

@login_required
def cart(request,slug):
	if Item.objects.filter(stock = 'In Stock'):
		if Cart.objects.filter(slug = slug).exists():
			quantity = Cart.objects.get(slug = slug).quantity
			quantity = quantity +1
			Cart.objects.filter(slug = slug).update(quantity = quantity)
		else:
			username = request.user
			data = Cart.objects.create(
				user = username,
				slug = slug,
				items = Item.objects.filter(slug = slug)[0]
				)
			data.save()
	else:
		messages.error(request, 'This item is out of stock')
		return redirect('/')

	return redirect('/')