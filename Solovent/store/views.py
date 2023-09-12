from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Basket,WorkDays
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from common.views import TitleMixin
from django.db.models import Q
from datetime import datetime


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
        search_guests = self.request.GET.get('search_guests')
        print(f'search_guests:{search_guests}')
        if len(search_time) == 0:
            search_time = '01-01-2023 12:00'
        # print(f'search_time TYPE:{type(search_time)}')
        # print(f'search_time VALUE:{search_time}')

        search_time_date = datetime.strptime(search_time, '%d-%m-%Y %H:%M')
        print(
               f' DATE:{search_time_date.date()}'
               f' YEAR:{search_time_date.year}'
               f' DAY:{search_time_date.day}'
               f' MONTH:{search_time_date.month}')
        #       f' Day week №:{datetime.isoweekday(search_time_date)}'
        #       f' HOUR:{search_time_date.time().hour}'
        #       f' MINUTE:{search_time_date.time().minute}'
        #       f' TYPE:{ type(search_time_date)}')
        day_list = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

        day_index = search_time_date.isoweekday()
        print(f'search_time NEW VALUE:{search_time_date} | {day_list[day_index-1]} H:{search_time_date.time().hour} ')
        # print(f'day:{queryset.filter(Q(work_days=day_index))}')
        # print(f'beg:{queryset.filter(Q(beginning_of_work_day_time__hour__lte=search_time_date.time().hour))}')
        # print(f'end:{queryset.filter(Q(end_of_work_day_time__hour__gt=search_time_date.time().hour))}')
        print(f'Product:{queryset.filter((Q(beginning_of_work_day_time__hour__lte=search_time_date.time().hour)| Q(end_of_work_day_time__hour__gt=search_time_date.time().hour)) & Q(work_days=day_index))}')

        return queryset.filter((Q(beginning_of_work_day_time__hour__lte=search_time_date.time().hour)
                               | Q(end_of_work_day_time__hour__gt=search_time_date.time().hour))
                               & Q(work_days=day_index)
                               & Q(number_of_quests__lte=search_guests))

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
