from django.urls import path, include
from store.views import catalog_view

app_name = 'store'

urlpatterns = [
    path('catalog/', catalog_view, name='catalog'),

]
