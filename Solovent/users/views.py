from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User, EmailVerification
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from store.models import Basket
from common.views import TitleMixin


# Class for registration user
class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'You have successfully registered!'
    title = 'Solovent - Registration'


# Class for login user
class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Solovent - Authorization'


# Class for profile user
class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Solovent - Profile'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Solovent - Confirmation'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        return super(EmailVerificationView)
