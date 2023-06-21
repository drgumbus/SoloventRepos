from django.shortcuts import render, redirect
from .forms import UserRegistration


# Функция регистрации пользователя
def registration_view(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('web/home')
    else:
        form = UserRegistration()
    return render(request, 'users/registration.html', {'form': form})


def authorization_view(request):
    return render(request, 'users/authorization.html')


def login_view(request):
    return render(request, 'users/login.html')


def profile_view(request):
    return render(request, 'users/profile.html')
