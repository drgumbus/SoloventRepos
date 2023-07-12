from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    """Categories to which the goods belong"""
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

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
    image = models.ImageField(upload_to='product_image/%Y/%m/%d', blank=True, verbose_name='Photo')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.DecimalField(max_length=15, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Availability')
    stock = models.DecimalField(max_length=10, decimal_places=2, verbose_name='Amount')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
