from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from shop.models import Collection, Product
from tags.models import TaggedItem 

# Create your views here.
def say_hello(request):
    
    return render(request, 'hello.html', {'name': "Przemek"})
