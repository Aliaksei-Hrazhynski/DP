from django.shortcuts import render
from cart.cartmodel import Cart
from datetime import datetime
from orders.models import Order, OrderItem


def order(request):
    cart = Cart(request)
    return render(request, "order.html", {'cart': cart})


def order_create(request):
    cart = Cart(request)
    first_name = request.POST.get('first_name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    date_delivery = request.POST.get('date_delivery')
    date_created = datetime.now()
    total_price = cart.get_total_price()
    if request.POST.get('delivery') == 1:
        delivery = 'Самовывоз'
    else:
        delivery = 'Доставка курьером'
    if request.POST.get('payment') == 1:
        payment = 'Оплата наличными'
    else:
        payment = 'Доставка курьером'
    order = Order.objects.create(first_name=first_name, phone=phone, email=email, delivery=delivery, payment=payment, total_price=total_price)
    order.save()
    for item in cart:
        OrderItem.objects.create(order=order,
                                 dish=item['dish'],
                                 price=item['price'],
                                 quantity=item['quantity'])
    cart.clear()
    return render(request, "index.html")
