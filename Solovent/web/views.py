from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

# импорт класса для регистрации
from django.views.generic import TemplateView

# Home page
def index(request):
    return render(request, 'web/index.html')


# About page
def about(request):
    return render(request, 'web/about.html')


def contacts(request):
    return render(request, 'web/contacts.html')





def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Sorry, page not found =(</h2>')

