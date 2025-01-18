from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static

from api.views import (
    AboutViewSet,
    NewViewSet,
    ProductViewSet,
    ProejctViewSet,
    products_view,
    index_view,
    about_view,
    news_view,
    product_detail_view
)

router = SimpleRouter()

router.register('news', NewViewSet, basename='news')
router.register('products', ProductViewSet, basename='products')
router.register('about', AboutViewSet, basename='about')
router.register('projects', ProejctViewSet, basename='projects')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls))
# ]
urlpatterns = [
    # URL для страницы с продуктами
    path('products/', products_view, name='products'),
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('news/', news_view, name='news'),
    path('admin/', admin.site.urls),
    path('product/<int:id>/', product_detail_view, name='product_detail'),
]

if settings.DEBUG:  # Убедитесь, что это в режиме разработки
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)