from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product, Category, Basket
from users.models import User


def catalog_view(request, category_id=None):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context = {
        'title': "Solovent - Store",
        'products': products,
        'cat_products': Category.objects.all(),
    }
    return render(request, 'store/catalog.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = Basket.objects.get(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
