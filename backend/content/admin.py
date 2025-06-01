from django.contrib import admin
from .models import (
    New,
    NewsImage,
    Product,
    ProductPDF,
    IndustryTag,
    ObjectTag,
    AboutIndex,
    Certificate,
    AboutCompany,
    CompanyPDF,
    LogoImage,
    Colleague,
    Region,
    Map,
    Project,
    ProjectProduct,
)


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ("name", "pub_date")
    inlines = [NewsImageInline]


class ProductPDFInline(admin.TabularInline):
    model = ProductPDF
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description")
    inlines = [ProductPDFInline]
    filter_horizontal = ("applying_objects", "industries")


@admin.register(IndustryTag)
class IndustryTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "slug")


@admin.register(ObjectTag)
class ObjectTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "slug")


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1


@admin.register(AboutIndex)
class AboutAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


class CompanyPDFInline(admin.TabularInline):
    model = CompanyPDF
    extra = 1


class LogoImageInline(admin.TabularInline):
    model = LogoImage
    extra = 1


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyPDFInline, LogoImageInline]


@admin.register(Colleague)
class ColleagueAdmin(admin.ModelAdmin):
    list_display = ("name", "position")


class ProjectProductInline(admin.TabularInline):
    model = ProjectProduct
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [ProjectProductInline]
    filter_horizontal = ("tag_object", "tag_sphere")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "coord_x", "coord_y")
    list_editable = ("is_active",)


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ("name",)
