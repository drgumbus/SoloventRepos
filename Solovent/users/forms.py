import uuid
from datetime import timedelta

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.utils.timezone import now

from users.models import User, EmailVerification


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you surname'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter you email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter you password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat you password'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you mobile'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user


class UserLoginForm(AuthenticationForm, forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you login'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter you password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you name',
        'class': 'profile-border-input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you surname',
        'class': 'profile-border-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': 'Choose avatar',
        'class': 'custom-file-input'
        }), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you mobile',
        'class': 'profile-border-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'phone_number')
