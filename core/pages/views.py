from django.shortcuts import render, redirect

from .models import Categories, Products


def index_view(request):
    context = {
        'title': f'Barker - Главная страница',
        'active': 'home'
    }

    return render(request, 'pages/index.html', context)
