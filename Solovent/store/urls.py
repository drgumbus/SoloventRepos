from django.urls import path, include
from store.views import CatalogListView, basket_add, basket_remove, CatalogDetailView, CatalogDateSearch
from django.conf.urls.static import static
from django.conf import settings

app_name = 'store'

urlpatterns = [
    # all catalog
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    # sorted catalog
    path('catalog/category/<int:category_id>/', CatalogListView.as_view(), name='category'),
    # search by date in catalog
    path('catalog/date/', CatalogDateSearch.as_view(), name='search_time'),
    # detail product
    path('catalog/<int:pk>', CatalogDetailView.as_view(), name='detail'),
    # add to basket
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    # removal from basket
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_rout=settings.MEDIA_ROOT)
