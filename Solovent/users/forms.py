from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms


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

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


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
        'placeholder': 'Enter you name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter you surname'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': 'Choose avatar',
        'class': 'custom-file-input'
        }), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter you mobile'})
                             )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'mobile')
