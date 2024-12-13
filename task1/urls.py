from django.urls import path
from . import views

urlpatterns = [
    # path('', views.sign_up_by_html, name='html_sign_up'),
    path('django_sign_up/', views.sign_up_by_django, name='django_sign_up'),
    path('', views.main_page, name='platform'),  # Главная страница
    path('shop/', views.shop_page, name='shop'),  # Магазин
    path('cart/', views.cart_page, name='cart'),  # Корзина
]
