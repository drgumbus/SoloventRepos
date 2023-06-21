from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static


# Список всех страниц сайта (При переходе на www.solovent.com/admin/ выдает страницу admin.site.urls)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),

] + static(settings.STATIC_URL, documen_root=settings.STATIC_ROOT)

