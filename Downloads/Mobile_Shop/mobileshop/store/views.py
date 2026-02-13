from django.shortcuts import render, redirect
from .models import Product, Cart
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    Cart.objects.create(user=request.user, product=product)
    return redirect('cart')


@login_required
def cart_view(request):
    items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'items': items})
