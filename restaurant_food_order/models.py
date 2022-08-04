from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class Food(models.Model):
#     type = (('main', 'Main dish'), ('side', 'Side dish'), ('dessert', 'Dessert'))
#     food_name = models.CharField(max_length=100)
#     food_type = models.CharField(max_length=10, choices=type)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#
#     def __str__(self):
#         return self.food_name

class MainDish(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.dish_name


class SideDish(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.dish_name


class Dessert(models.Model):
    desert_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.desert_name


class Order(models.Model):
    main_dish = models.CharField(max_length=100)
    main_dish_qty = models.IntegerField()
    side_dish = models.CharField(max_length=100)
    side_dish_qty = models.IntegerField()
    desert = models.CharField(max_length=100)
    desert_qty = models.IntegerField()
    order_time = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_pay = models.BooleanField()

    def __str__(self):
        return self.main_dish

MainDish.objects.create(
    dish_name='aaaa',
    price='11.00'
)
