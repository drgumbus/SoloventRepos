from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to="users_image/%Y/%m/%d", null=True, blank=True, max_length=255)

