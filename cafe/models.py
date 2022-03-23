from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)

    class Meta:
        ordering = ('id',)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(unique=True, max_length=75)

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    title = models.CharField(unique=True, max_length=75, verbose_name='Название блюда')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name='Цена блюда')
    discount = models.PositiveIntegerField(blank=True, null=True, verbose_name='Размер скидки')
    dish_weight = models.PositiveIntegerField(null=False, verbose_name='Вес (в граммах)')
    product = models.ManyToManyField(Product, verbose_name='Используемые продукты')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/dish/', null=True, verbose_name='Фото блюда')
    flag_promotion = models.BooleanField(blank=True, verbose_name='Акция')
    flag_popular = models.BooleanField(blank=True, verbose_name='Популярное')
    flag_novelty = models.BooleanField(blank=True, verbose_name='Новинка')
    flag_available = models.BooleanField(blank=True, default=True, verbose_name='Доступно ли блюдо к продаже')

    class Meta:
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title

    def new_price(self, price, discount):
        return self.price * (100 - self.discount)
