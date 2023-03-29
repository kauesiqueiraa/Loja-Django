from django.shortcuts import render
from .models import Category


def home(request):
    return render(request, 'index.html')


def category_list(request):
    data = Category.objects.all().order_by('-id')

    return render(request, 'category_list.html', {'data': data})


def marca_list(request):
    return render(request, 'marca_list.html')


def product_list(request):
    return render(request, 'product_list.html')
