from django.urls import path, include
from . import views as web_views


# Список всех страниц сайта (При переходе на www.solovent.com/admin/ выдает страницу admin.site.urls)
urlpatterns = [
    path('', web_views.index, name='home'),
    path('about/', web_views.about, name='about'),
    path('contacts/', web_views.contacts, name='contacts'),
    path('users/', include('users.urls')),
]