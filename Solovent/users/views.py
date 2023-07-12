from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from django.contrib import auth


# Функция регистрации пользователя
def registration_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'Solovent - Registration', 'form': form}
    return render(request, 'users/registration.html', context)


# Функция логирования пользователя
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {'title': 'Solovent - Login', 'form': form}
    return render(request,  'users/login.html', context)


# Функция профиля пользователя
def profile_view(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Solovent - Profile', 'form': form}
    return render(request, 'users/profiletest.html', context)


def authorization_view(request):
    return render(request, 'users/authorization.html')
