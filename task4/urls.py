from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='platform4'),  # Главная страница
    path('shop/', views.shop_page, name='shop4'),  # Магазин
    path('cart/', views.cart_page, name='cart4'),  # Корзина
]
