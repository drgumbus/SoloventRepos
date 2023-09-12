from django.contrib import admin
from .models import Category, Product, WorkDays

# Register your models here.

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ['work_days']

    fieldsets = (

        (None, {
            "fields": (
                'name', 'category', 'price', 'number_of_quests',
            )
        }),

        (None, {
            "fields": (
                ("beginning_of_work_day_time", "end_of_work_day_time",'work_days',),
            )
        }),
    )


