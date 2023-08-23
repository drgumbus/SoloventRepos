from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product, Category, Basket
from users.models import User


def catalog_view(request):
    context = {
        'products': Product.objects.all(),
        'cat_products': Category.objects.all(),
    }
    return render(request, 'store/catalog.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
