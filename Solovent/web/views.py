from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views.generic.base import TemplateView

from common.views import TitleMixin


# Home page
class IndexView(TitleMixin, TemplateView):
    template_name = 'web/index.html'
    title = 'Solovent - Home'


def contacts_view(request):
    return render(request, 'web/contacts.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Sorry, page not found =(</h2>')

