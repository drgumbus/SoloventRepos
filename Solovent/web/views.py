from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def web_view(request):
    return render(request, 'web/about.html')


# Home page
def index_view(request):
    context = {'title': 'Solovent', 'username': 'Din'}
    return render(request, 'web/index.html', context)


# About page
def about_view(request):
    return render(request, 'web/about.html')


def contacts_view(request):
    return render(request, 'web/contacts.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Sorry, page not found =(</h2>')

