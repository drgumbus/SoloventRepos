from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Basket
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from common.views import TitleMixin
from django.db.models import Q
from datetime import date


# Catalog products
class CatalogListView(TitleMixin, ListView):
    model = Product
    template_name = 'store/catalog.html'
    title = 'Solovent - Store'
    print(date.today())

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
        context['search'] = self.request.GET.get('search')
        return context


# Details product view
class CatalogDetailView(TitleMixin, DetailView):
    model = Product
    template_name = 'store/catalog_detail.html'
    title = 'Solovent - Detail'


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
