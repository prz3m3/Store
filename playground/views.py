from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Product

# Create your views here.
def say_hello(request):
    try:
        queryset = Product.objects.filter()
    except ObjectDoesNotExist:
        pass

    return render(request, 'hello.html', {'name': "Przemek", 'products':list(queryset)})
