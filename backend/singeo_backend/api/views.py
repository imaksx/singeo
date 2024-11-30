from rest_framework import viewsets

from content.models import New, Product, About
from .serializers import NewSerializer, ProductSerializer, AboutSerializer


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    # будет нужна пагинация
    # нужен будет доступ по админке на все методы, кроме GET


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # будет нужна пагинация
    # нужен будет доступ по админке на все методы, кроме GET


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    # нужен будет доступ по админке на все методы, кроме GET


# адреса с get-запросами, которые должны работать:
# 1. singeo/news/ - страница со всеми новостями
# 2. singep/news/{news_id}/ - страница с отдельной новостью
# 3. singeo/products/ -  страница со всеми продуктами
# 4. singeo/products/{product_id}/ - страница с отдельным товаром
# 5. singeo/about/ - страница с разделом 'о нас'

# остальные методы доступны только админу