from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static

from api.views import (
    # AboutViewSet,
    # NewViewSet,
    # ProductViewSet,
    # ProejctViewSet,
    index_view,
    about_view,
    products_view,
    product_detail_view,
    projects_view,
    project_detail_view,
    news_view,
    new_detail_view,
)

router = SimpleRouter()

# router.register('news', NewViewSet, basename='news')
# router.register('products', ProductViewSet, basename='products')
# router.register('about', AboutViewSet, basename='about')
# router.register('projects', ProejctViewSet, basename='projects')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls))
# ]
urlpatterns = [
    # URL для страницы с продуктами
    path('about/', about_view, name='about'),
    path('', index_view, name='index'),
    path('products/', projects_view, name='projects'),
    path('projects/<int:id>/', project_detail_view, name='project_detail'),
    path('product/<int:id>/', product_detail_view, name='product_detail'),
    path('projects/', products_view, name='products'),
    path('news/', news_view, name='news'),
    path('news/<int:id>/', new_detail_view, name='news_detail'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:  # Убедитесь, что это в режиме разработки
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
