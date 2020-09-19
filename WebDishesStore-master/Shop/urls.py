from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'Shop'

urlpatterns = [
    path('', views.forum, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('shop-detail/', views.shop_detail, name='shop-detail'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact-us'),
    path('about/', views.about, name='about'),
]
