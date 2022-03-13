from decimal import Decimal
from django.conf import settings
from ..cafe.models import Dish


class Cart(object):
    def __int__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, dish, quantity=1, update_quantity=False):
        """
        Add dish in the cart or update his quantity
        """
        dish_id = str(dish.id)
        if dish_id not in self.cart:
            self.cart[dish_id] = {'quantity': 0, 'price': str(dish.price)}
        if update_quantity:
            self.cart[dish_id]['quantity'] = quantity
        else:
            self.cart[dish_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Update session cart
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, dish):
        """
        Removing a dish from the cart
        """
        dish_id = str(dish.id)
        if dish_id in self.cart:
            del self.cart[dish_id]
            self.save()

    def __iter__(self):
        """
        Iterating through the items in the cart and getting the dishes from the database
        """
        dish_ids = self.cart.keys()
        dishes = Dish.objects.filter(id__in=dish_ids)
        for dish in dishes:
            self.cart[str(dish.id)]['dish'] = 'dish'
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

    def __len__(self):
        """
        Counting all dishes in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculate the cost of dishes in the cart
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Remove dish from session
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
