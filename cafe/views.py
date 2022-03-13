from django.template import loader
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Dish

'''def index(request):
    template = loader.get_template('index.html')
    context = {'dishs': Dish.objects.all()}
    return HttpResponse(template.render(context, request))
    
def payment(request):
    template = loader.get_template('payment.html')
    context = {}
    return HttpResponse(template.render(context, request))    
'''


def index(request):
    context = {'dishs': Dish.objects.all()}
    return render(request, "index.html", context)


def payment(request):
    return render(request, "payment.html")


def dish_details(request, pk):
    dish = Dish.objects.get(id=pk)
    context = {"dish": dish}
    return render(request, "dish_details.html", context)

