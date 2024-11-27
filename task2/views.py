from django.shortcuts import render
from django.views import View

# Create your views here.
# функциональное представление
def function_view(request):
    return render(request, 'second_task/function_view.html')

# классовое представление
class ClassView(View):
    def get(selfself, request):
        return render(request, 'second_task/class_view.html')
