from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='platform'),  # Главная страница
    path('shop/', views.shop_page, name='shop'),  # Магазин
    path('cart/', views.cart_page, name='cart'),  # Корзина
]
