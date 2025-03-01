from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from content.models import New, Product, About, Project
# from .serializers import NewSerializer, ProductSerializer, AboutSerializer, ProjectSerializer


def about_view(request):
    about = About.objects.first()  # Получаем первую запись о компании
    return render(request, 'about.html', {'about': about})


def index_view(request):
    products = Product.objects.all()  # Получаем все продукты
    projects = Project.objects.all()  # Получаем все проекты
    # Получаем информацию о компании (предполагается, что она одна)
    about = About.objects.first()

    return render(request, 'main/index.html', {
        'products': products,
        'projects': projects,
        'about': about,  # Передаем экземпляр About в контекст
    })


def project_list(request):
    # НУЖДАЕТСЯ В ОТЛАДКЕ
    projects = Project.objects.all()

    # Получаем все уникальные продукты, используемые в проектах
    products_used_in_projects = Product.objects.filter(
        projectproduct__project__in=projects).distinct()

    context = {
        'projects': projects,
        # Передаем продукты в качестве фильтров
        'sensor_types': products_used_in_projects,
    }
    return render(request, 'main/projects.html', context)


def products_view(request):
    products = Product.objects.all()
    return render(request, 'main/products.html', {'products': products})


def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'main/product_detail.html', {'product': product})


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})


def project_detail_view(request, id):
    project = get_object_or_404(Product, id=id)  # Получаем продукт по ID
    return render(request, 'main/project_detail.html', {'product': project})


def news_view(request):
    # НЕ РАБОТАЕТ СОРТИРОВКА
    news = New.objects.all().order_by('-pub_date')

    return render(request, 'main/news.html', {'news': news})


def new_detail_view(request, id):
    article = get_object_or_404(New, id=id)  # Получаем новость по ID
    # Передаем article в контекст
    return render(request, 'main/news_detail.html', {'article': article})


# адреса с get-запросами, которые должны работать:
# 1. singeo/ - главная страница
# 2. singeo/about/ - страница с разделом 'о нас'
# 3. singeo/products/ -  страница со всеми продуктами
# 4. singeo/products/{product_id}/ - страница с отдельным товаром
# 5. singeo/project/ - страница с продуктами
# 6. singeo/projects/{project_id} - страница с отдельным проектом
# 7. singeo/news/ - страница со всеми новостями
# 8. singep/news/{news_id}/ - страница с отдельной новостью
# остальные методы доступны только админу
