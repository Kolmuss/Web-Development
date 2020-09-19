from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *


def getProductByPage(page=0, per_page=5):
    product = Paginator(Product.objects.all(), per_page)
    return product.get_page(page)


def forum(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/index.html', content)


def shop(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/shop.html', content)


def cart(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/cart.html', content)


def checkout(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/checkout.html', content)


def wishlist(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/wishlist.html', content)


def shop_detail(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/shop-detail.html', content)


def service(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/service.html', content)


def contact(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/contact-us.html', content)


def about(request):
    content = {'product': Product.objects.all()}
    return render(request, 'Shop/about.html', content)
