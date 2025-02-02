from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from content.models import New, Product, About, Project
from .serializers import NewSerializer, ProductSerializer, AboutSerializer, ProjectSerializer


def products_view(request):
    products = Product.objects.all()  # Получаем все продукты из базы данных
    return render(request, 'main/products.html', {'products': products})


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


def about_view(request):
    return render(request, 'main/about.html')


def news_view(request):
    return render(request, 'main/news.html')


def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)  # Получаем продукт по ID
    return render(request, 'main/product_detail.html', {'product': product})


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    http_method_names = ['get']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    http_method_names = ['get']


class ProejctViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


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
