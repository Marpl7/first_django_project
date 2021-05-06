from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    path = os.getcwd()
    msg = os.listdir(path)
    template_name = 'files.html'
    context = {
        'msg': msg
    }
    return render(request, template_name, context)