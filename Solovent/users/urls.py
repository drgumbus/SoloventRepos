from django.urls import path, include
from users.views import login_view, profile_view, registration_view, authorization_view

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('authorization/', authorization_view, name='authorization'),
]
