from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cafe.models import Dish


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    phone = PhoneNumberField(null=False, blank=False)
    email = models.EmailField()
    address_delivery = models.CharField(max_length=250)
    """date_delivery = models.DateTimeField()
    date_created = models.DateTimeField()"""
    moderation = models.BooleanField(default=False)
    delivery = models.CharField(max_length=50, null=True, blank=True)
    payment = models.CharField(max_length=50, null=True, blank=True)
    total_price = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
