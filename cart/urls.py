from django.urls import path
from cart.views import cart_add, cart_remove, cart_details


urlpatterns = [
    path('cart_details/', cart_details, name='cart_details'),
    path('cart_add/', cart_add, name='cart_add'),
    path('cart_remove/', cart_remove, name='cart_remove'),

]
