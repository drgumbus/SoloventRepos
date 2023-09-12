from django.db import models
from users.models import User
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category_image/%Y/%m/%d', blank=True, verbose_name='Category_icon')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class WorkDays(models.Model):
    MON = 'MONDAY'
    TUE = 'TUESDAY'
    WED = 'WEDNESDAY'
    THU = 'THURSDAY'
    FRI = 'FRIDAY'
    SAT = 'SATURDAY'
    SUN = 'SUNDAY'

    # DAYS
    DAYS_OF_WORK = [
        (MON, 'Monday'),
        (TUE, 'Tuesday '),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
        (SUN, 'Sunday'),
    ]

    work_day = models.CharField(
        verbose_name='name day',
        choices=DAYS_OF_WORK,
        max_length=9,
        default=MON,
    )

    class Meta:
        verbose_name = 'Work day'
        verbose_name_plural = 'Work days'

    def __str__(self):
        return self.work_day


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Products', on_delete=models.CASCADE,
                                 verbose_name='Category')
    name = models.CharField(max_length=250, db_index=True, verbose_name='Product')
    slug = models.SlugField(max_length=250, db_index=True)
    image = models.ImageField(upload_to='product_image/%Y/%m/%d', blank=True, verbose_name='Photo')
    description = models.TextField(max_length=500, blank=True, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Availability')
    stock = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    
    beginning_of_work_day_time = models.TimeField(default=now,
                                                  verbose_name='beginning of work time')
    end_of_work_day_time = models.TimeField(default=now,
                                            verbose_name='end of work time')

    work_days = models.ManyToManyField(WorkDays, blank=True, related_name='work_days')

    number_of_quests = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'

    def get_work_days(self):
        pass


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

