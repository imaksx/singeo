from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import (
    AboutViewSet,
    NewViewSet,
    ProductViewSet
)

router = SimpleRouter()

router.register('news', NewViewSet, basename='news')
router.register('products', ProductViewSet, basename='products')
router.register('about', AboutViewSet, basename='about')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
