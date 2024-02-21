from django.shortcuts import render,redirect

from . import models
from .models import SliderItem , Test
from django.db.models import Q
# Create your views here.


def home(request):
    products = Test.objects.all()
    chunk_size = 3
    chunks = [products[i:i + chunk_size] for i in range(0, len(products), chunk_size)]
    return render(request, "home/home.html", {'chunks': chunks, 'products': products})


def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Test.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
        )
    return render(request, 'home/search_results.html', {'query': query, 'results': results})


def slider_view(request):
    slider_items = SliderItem.objects.all()
    return render(request, 'slider.html', {'slider_items': slider_items})
