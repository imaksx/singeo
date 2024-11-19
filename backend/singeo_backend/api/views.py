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
