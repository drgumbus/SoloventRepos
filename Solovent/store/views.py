from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Basket
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from common.views import TitleMixin
from django.db.models import Q
import datetime

# Catalog products
class CatalogListView(TitleMixin, ListView):
    model = Product
    template_name = 'store/catalog.html'
    title = 'Solovent - Store'

    def get_queryset(self):
        queryset = super(CatalogListView, self).get_queryset()
        search_query = self.request.GET.get('search')
        category_id = self.kwargs.get('category_id')

        if search_query:
            return queryset.filter(Q(name__icontains=search_query)
                                   | Q(description__icontains=search_query)
                                   | Q(category__name__icontains=search_query))
        elif category_id:
            return queryset.filter(category_id=category_id)
        else:
            return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogListView, self).get_context_data()
        context['cat_products'] = Category.objects.all()
        return context


# Details product view
class CatalogDetailView(TitleMixin, DetailView):
    model = Product
    template_name = 'store/catalog_detail.html'
    title = 'Solovent - Detail'


class CatalogDateSearch(TitleMixin, ListView):
    model = Product
    template_name = 'store/catalog.html'
    title = 'Solovent - Store'

    def get_queryset(self):
        queryset = super(CatalogDateSearch, self).get_queryset()
        search_time = self.request.GET.get('search_time')
        print(f'search_time TYPE:{type(search_time)}')
        print(f'search_time VALUE:{search_time}')

        search_time_day = int(search_time[:2])
        search_time_month = int(search_time[3:5])
        search_time_year = int(search_time[6:10])
        search_time_hour = int(search_time[11:13])
        search_time_minute = int(search_time[14:17])

        # print(f'search_time DAY:{search_time_day}')
        # print(f'search_time MONTH:{search_time_month}')
        # print(f'search_time YEAR:{search_time_year}')
        #
        # print(f'search_time HOUR:{search_time_hour}')
        # print(f'search_time MINUTE:{search_time_minute}')

        return queryset.filter(beginning_of_work_day_time__hour__lte=search_time_hour)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogDateSearch, self).get_context_data()
        context['cat_products'] = Category.objects.all()
        return context


# Add from basket
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


# removal from basket
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
