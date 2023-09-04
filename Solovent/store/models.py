from django.db import models
from django.urls import reverse
from users.models import User
# Create your models here.
from django.utils import timezone

class Category(models.Model):
    """Categories to which the goods belong"""
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_image/%Y/%m/%d', blank=True, verbose_name='Category_icon')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product description model"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 verbose_name='Select a category')
    name = models.CharField(max_length=250, db_index=True, verbose_name='Name')
    slug = models.SlugField(max_length=250, db_index=True)

    # from_time_work = models.DateTimeField(default=timezone.now)
    # to_time_work = models.DateTimeField(default=timezone.now)

    image = models.ImageField(upload_to='product_image/%Y/%m/%d', blank=True, verbose_name='Photo')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Availability')
    stock = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Basket for {self.user.username} | Product: {self.product.name }'

    def sum(self):
        return self.product.price * self.quantity

