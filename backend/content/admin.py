from django.contrib import admin
from .models import (New, Product,
                     AboutIndex,
                     Project,
                     ProjectProduct,
                     ProjectRegion,
                     Region,
                     Map,
                     MapRegion,
                     Certificate,
                     TechnicalDescription,
                     AboutCompany, Colleague,
                     LogoImage,
                     CompanyPDF, NewsImage,
                     ProductPDF, ObjectTagForProject, IndustryTagForProject
                     )


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1  # Количество пустых форм для добавления новых сертификатов


@admin.register(AboutIndex)
class AboutAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['image']


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1  # Количество пустых форм для добавления новых изображений


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    inlines = [NewsImageInline]  # Добавляем встроенные модели


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('news', 'image')


# Удалите следующую строку, чтобы избежать ошибки
# admin.site.register(NewsImage)  # Эта строка вызывает ошибку

# Регистрация остальных моделей
admin.site.register(Product)
admin.site.register(Project)
admin.site.register(Region)
admin.site.register(ProjectProduct)
admin.site.register(ProjectRegion)
admin.site.register(Map)
admin.site.register(MapRegion)
admin.site.register(TechnicalDescription)
admin.site.register(AboutCompany)
admin.site.register(Colleague)
admin.site.register(LogoImage)
admin.site.register(CompanyPDF)
admin.site.register(ProductPDF)
admin.site.register(IndustryTagForProject)
admin.site.register(ObjectTagForProject)
