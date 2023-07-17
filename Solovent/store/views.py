from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product, Category


def catalog_view(request):
    products = Product.objects.all()
    cat_products = Category.objects.all()

    return render(request, 'store/catalog.html', {'products': products, 'cat_products': cat_products})
