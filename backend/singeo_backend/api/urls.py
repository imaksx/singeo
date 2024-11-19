from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (
    AboutViewSet,
    NewViewSet,
    ProductViewSet
)

router = SimpleRouter()

router.register('news', NewViewSet, basename='news')
router.register('products', ProductViewSet, basename='products')
router.register('about', AboutViewSet, basename='about')

urlpatterns = [
    path('', include(router.urls))
]
