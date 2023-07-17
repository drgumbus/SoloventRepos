from django.urls import path, include
from store.views import catalog_view
from django.conf.urls.static import static
from django.conf import settings

app_name = 'store'

urlpatterns = [
    path('catalog/', catalog_view, name='catalog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_rout=settings.MEDIA_ROOT)
