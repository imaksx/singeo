from django.contrib import admin

from .models import New, Product, About, Project, ProjectProduct, ProjectRegion, Region, Map, MapRegion, Certificate, TechnicalDescription, AboutCompany, Colleague, LogoImage, CompanyPDF

class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1  # Количество пустых форм для добавления новых сертификатов


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['image']


admin.site.register(New)
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
