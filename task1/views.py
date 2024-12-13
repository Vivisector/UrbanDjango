from django.shortcuts import render
from django.views import View

# Гл страница
def main_page(request):
    return render(request, 'first_task/platform.html')

#
# Страница Магазина
def shop_page(request):
    # items = {# список товаров
    #     'item1': 'Игровая мышь, 1500 р.',
    #     'item2': 'Клавиатура, 700 р.',
    #     'item3': 'Игровой монитор, 25000 р.'
    # }
    # return render(request, 'fourth_task/games.html', {'items': items})
    context = {'games': ["Atomic Heart", "Cyberpunk 2077", "SuperPuperMario 1.0"]}
    return render(request, "first_task/games.html", context)

# страница Корзина
def cart_page(request):
    cart_info = {
        'item_count': 3,
        'total_price': '27200 руб.'
    }
    return render(request, 'first_task/cart.html', {'cart_info': cart_info})

from .forms import UserRegister

# Псевдо-список существующих пользователей
users = ['user1', 'user2', 'user3']


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        age = int(request.POST.get('age', 0))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif age > 120:  # ограничение на максимальный возраст
            info['error'] = 'Возраст должен быть реальным (до 120 лет)'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f'Приветствуем, {username}!'
            users.append(username)

    return render(request, 'first_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['success'] = f'Приветствуем, {username}!'
            users.append(username)

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)
