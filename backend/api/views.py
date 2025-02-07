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


def products_view(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных
    return render(request, 'main/products.html', {'products': products})


def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)  # Получаем продукт по ID
    return render(request, 'main/product_detail.html', {'product': product})


def projects_view(request):
    projects = Project.objects.all()  # Получаем все проектыв из базы данных
    return render(request, 'main/projects.html', {'projects': projects})


def project_detail_view(request, id):
    project = get_object_or_404(Product, id=id)  # Получаем продукт по ID
    return render(request, 'main/project_detail.html', {'product': project})


def news_view(request):
    # Получаем все новости и сортируем по дате публикации (pub_date) от самой ранней к самой поздней
    # Используем 'pub_date' для сортировки
    news = New.objects.all().order_by('-pub_date')

    return render(request, 'main/news.html', {'news': news})


def new_detail_view(request, id):
    article = get_object_or_404(New, id=id)  # Получаем новость по ID
    # Передаем article в контекст
    return render(request, 'main/news_detail.html', {'article': article})


# class NewViewSet(viewsets.ModelViewSet):
#     queryset = New.objects.all()
#     serializer_class = NewSerializer
#     http_method_names = ['get']


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     http_method_names = ['get']


# class AboutViewSet(viewsets.ModelViewSet):
#     queryset = About.objects.all()
#     serializer_class = AboutSerializer
#     http_method_names = ['get']


# class ProejctViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


# адреса с get-запросами, которые должны работать:
# 1. singeo/news/ - страница со всеми новостями
# 2. singep/news/{news_id}/ - страница с отдельной новостью
# 3. singeo/products/ -  страница со всеми продуктами
# 4. singeo/products/{product_id}/ - страница с отдельным товаром
# 5. singeo/about/ - страница с разделом 'о нас'
# 6. singeo/ - главная страница
# 7. singeo/project/ - страница с продуктами
# 8. singeo/projects/{project_id} - страница с отдельным продуктом

# остальные методы доступны только админу
