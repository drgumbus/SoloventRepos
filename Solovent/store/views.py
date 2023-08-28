from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Basket
from django.views.generic.list import ListView
from common.views import TitleMixin

# Catalog products
class CatalogListView(TitleMixin, ListView):
    model = Product
    template_name = 'store/catalog.html'
    title = 'Solovent - Store'

    def get_queryset(self):
        queryset = super(CatalogListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogListView, self).get_context_data()
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
