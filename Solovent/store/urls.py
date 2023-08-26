from django.urls import path, include
from store.views import catalog_view, basket_add, basket_remove
from django.conf.urls.static import static
from django.conf import settings

app_name = 'store'

urlpatterns = [
    path('catalog/', catalog_view, name='catalog'),
    path('catalog/category/<int:category_id>/', catalog_view, name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_rout=settings.MEDIA_ROOT)
