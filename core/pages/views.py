from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import Categories, Products, Worker


def index_view(request):
    total_worker = Worker.objects.exclude(position='с').count()
    total_product = Products.objects.all().count()
    context = {
        'title': f'Barker - Главная страница',
        'total_worker': total_worker,
        'total_product': total_product,
        'active': 'home'
    }

    return render(request, 'pages/index.html', context)


def team_view(request):
    worker_intern = Worker.objects.filter(position='с')
    worker_experienced = Worker.objects.exclude(position='с')

    context = {
        'title': 'Команда',
        'active': 'team',
        'title_header': 'Наша команда',
        'worker_experienced': worker_experienced,
        'worker_intern': worker_intern
    }

    return render(request, 'pages/team.html', context)


class ListProductPages(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'pages/list_product.html'
    paginate_by = 4
    extra_context = {
        'title': 'Продукты Barker',
        'title_header': 'Наши продукты'
    }


class ShowProductByCategoryId(ListProductPages):
    def get_queryset(self):
        product = Products.objects.filter(category_id=self.kwargs['cat_id'])
        return product

    def get_context_object_name(self, object_list):
        context = super().get_context_object_name()
        category = Categories.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Barker Категория: {category.name}'
        return context
