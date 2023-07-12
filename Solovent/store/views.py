from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def catalog_view(request):
    return render(request, 'store/catalog.html')
