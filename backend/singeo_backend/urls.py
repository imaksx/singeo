from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static

from api.views import (
    index_view,
    products_view,
    product_detail_view,
    project_list,
    project_detail_view,
    news_view,
    new_detail_view,
    about_company_view,
    download_certificates
)

router = SimpleRouter()

urlpatterns = [
    path('about/', about_company_view, name='about'),
    path('', index_view, name='index'),
    path('projects/', project_list, name='projects'),
    path('projects/<int:id>/', project_detail_view, name='project_detail'),
    path('product/<int:id>/', product_detail_view, name='product_detail'),
    path('products/', products_view, name='products'),
    path('news/', news_view, name='news'),
    path('news/<int:id>/', new_detail_view, name='news_detail'),
    path('admin/', admin.site.urls),
    path('download-certificates/', download_certificates,
         name='download_certificates')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
