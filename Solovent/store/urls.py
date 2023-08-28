from django.urls import path, include
from store.views import CatalogListView, basket_add, basket_remove
from django.conf.urls.static import static
from django.conf import settings

app_name = 'store'

urlpatterns = [
    # all catalog
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    # catalog by category
    path('catalog/category/<int:category_id>/', CatalogListView.as_view(), name='category'),
    # add to basket
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    # removal from basket
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_rout=settings.MEDIA_ROOT)
