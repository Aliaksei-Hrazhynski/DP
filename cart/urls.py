from django.urls import path
from cart.views import cart_add, cart_remove, cart_details, cart_clear, cart_update


urlpatterns = [
    path('cart_details/', cart_details, name='cart_details'),
    path('cart_add/', cart_add, name='cart_add'),
    path('cart_update/', cart_update, name='cart_update'),
    path('cart_remove/', cart_remove, name='cart_remove'),
    path('cart_clear/', cart_clear, name='cart_clear'),

]
