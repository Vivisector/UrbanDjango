"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.shortcuts import render
# from UrbanDjango.task3 import views

# from django.http import HttpResponse


# Временная функция для отображения текста на главной странице
# def home(request):
#     # return HttpResponse("<h1>Добро пожаловать на главную страницу!</h1>")
#     return render(request, "home.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task1.urls')),  # маршруты из task1
    path('task1/', include('task1.urls')),  # маршруты из task1
    path('task2/', include('task2.urls')),  # маршруты из task2
    # path('task3/', include('task3.urls')),  # маршруты из task2
    path('task4/', include('task4.urls')),  # маршруты из task4
    path('task5/', include('task5.urls')),  # маршруты из task5

]
