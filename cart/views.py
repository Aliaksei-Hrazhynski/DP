from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from cafe.models import Dish
from .cartmodel import Cart
from .forms import CartAddDishForm


@require_POST
def cart_add(request):
    dish_id = request.POST.get('dish_id')
    update_quantity = request.POST.get('update_quantity')
    quantity = request.POST.get('quantity')
    print(dish_id, update_quantity, quantity)
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


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_details')


def cart_details(request):
    cart = Cart(request)
    return render(request, 'cart_details.html', {'cart': cart})


def cart_update(request):
    dish_id = request.POST.get('dish_id')
    update_quantity = request.POST.get('update_quantity')
    quantity = int(request.POST.get('quantity'))
    cart = Cart(request)
    dish = get_object_or_404(Dish, id=dish_id)
    cart.add(dish=dish, quantity=quantity, update_quantity=update_quantity)
    return redirect('cart_details')
