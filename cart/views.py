from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cafe.models import Dish
from .cartmodel import Cart
from .forms import CartAddDishForm


@require_POST
def cart_add(request):
    dish_id = request.POST.get('dish_id')
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    form = CartAddDishForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(dish=dish, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart_details')


def cart_remove(request):
    dish_id = request.POST.get('id')
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.remove(dish)
    return redirect('cart_details')


def cart_details(request):
    cart = Cart(request)
    return render(request, 'cart_details.html', {'cart': cart})
