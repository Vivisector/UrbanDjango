from django.shortcuts import render
from django.views import View

# Гл страница
def main_page(request):
    return render(request, 'fourth_task/platform.html')

#
# Страница Магазина
def shop_page(request):
    # items = {# список товаров
    #     'item1': 'Игровая мышь, 1500 р.',
    #     'item2': 'Клавиатура, 700 р.',
    #     'item3': 'Игровой монитор, 25000 р.'
    # }
    # return render(request, 'fourth_task/games.html', {'items': items})
    context = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    return render(request, "fourth_task/games.html", context)

# страница Корзина
def cart_page(request):
    cart_info = {
        'item_count': 3,
        'total_price': '27200 руб.'
    }
    return render(request, 'fourth_task/cart.html', {'cart_info': cart_info})
# Create your views here.
