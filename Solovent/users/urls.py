from django.urls import path, include
from users import views as users_views




urlpatterns = [
    path('profile/', users_views.profile_view, name='profile'),
    path('login/', users_views.login_view, name='login'),
    path('registration/', users_views.registration_view, name='registration'),
    path('authorization/', users_views.authorization_view, name='authorization'),
]