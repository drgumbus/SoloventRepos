from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    image = models.ImageField(upload_to="users_image/%Y/%m/%d", null=True, blank=True, max_length=255)
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        send_mail(
            'Subject here',
            'Here is the message',
            'from@example.com',
            [self.user.email],
            fail_silently=False
        )
