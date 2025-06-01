from django.utils import timezone
from django.shortcuts import render, get_object_or_404
import os
import zipfile
from django.http import HttpResponse
from django.conf import settings

from content.models import (
    New,
    Product,
    Project,
    AboutCompany,
    Colleague,
    Certificate,
    IndustryTag,
    ObjectTag,
)

from api.utils import format_multiline_text


def download_certificates(request):
    """Функция для скачивания архива с сертификатами."""

    certificates = Certificate.objects.all()
    zip_filename = "certificates.zip"
    zip_filepath = os.path.join(settings.MEDIA_ROOT, zip_filename)

    with zipfile.ZipFile(zip_filepath, "w") as zip_file:
        for certificate in certificates:
            if certificate.image:
                zip_file.write(
                    certificate.image.path, os.path.basename(certificate.image.path)
                )

    with open(zip_filepath, "rb") as zip_file:
        response = HttpResponse(zip_file.read(), content_type="application/zip")
        response["Content-Disposition"] = f"attachment; filename={zip_filename}"

    os.remove(zip_filepath)

    return response


def about_company_view(request):
    about_company = AboutCompany.objects.first()

    established_year = 2019
    current_year = timezone.now().year
    years_in_market = current_year - established_year
    certificates = Certificate.objects.all()
    project_count = Project.objects.count()
    logo_images = about_company.logo_images.all()
    company_pdfs = about_company.pdfs.all()
    colleagues = Colleague.objects.all()

    context = {
        "about_company": about_company,
        "colleagues": colleagues,
        "years_in_market": years_in_market,
        "project_count": project_count,
        "certificates": certificates,
        "logo_images": logo_images,
        "company_pdfs": company_pdfs,
    }

    return render(request, "main/about_company.html", context)


def index_view(request):
    products = Product.objects.all()
    projects = Project.objects.all()

    return render(
        request,
        "main/index.html",
        {
            "products": products,
            "projects": projects,
        },
    )


def project_list(request):
    projects = Project.objects.all()

    # Получаем все уникальные теги объектов применения
    object_tags = ObjectTag.objects.all()

    # Получаем все уникальные теги отраслей
    industry_tags = IndustryTag.objects.all()

    # Получаем все уникальные продукты, используемые в проектах (если нужно)
    products_used_in_projects = Product.objects.filter(
        projectproduct__project__in=projects
    ).distinct()

    context = {
        "projects": projects,
        "object_tags": object_tags,
        "industry_tags": industry_tags,
        "sensor_types": products_used_in_projects,  # если все еще нужно
    }
    return render(request, "main/projects.html", context)


# старый рабочий до попытки завести фильтрацию
# def project_list(request):
#     # НУЖДАЕТСЯ В ОТЛАДКЕ
#     projects = Project.objects.all()

#     # Получаем все уникальные продукты, используемые в проектах
#     products_used_in_projects = Product.objects.filter(
#         projectproduct__project__in=projects).distinct()

#     context = {
#         'projects': projects,
#         # Передаем продукты в качестве фильтров
#         'sensor_types': products_used_in_projects,
#     }
#     return render(request, 'main/projects.html', context)


def products_view(request):
    products = Product.objects.all()
    return render(request, "main/products.html", {"products": products})


def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)  # Получаем продукт по ID
    related_projects = product.project_set.all()  # Получаем связанные проекты

    return render(
        request,
        "main/product_detail.html",
        {
            "product": product,
            "related_projects": related_projects,
            "specifications": format_multiline_text(product.specifications),
        },
    )


def projects_view(request):
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects": projects})


def project_detail_view(request, id):
    project = get_object_or_404(Project, id=id)  # Получаем продукт по ID
    return render(request, "main/project_detail.html", {"project": project})


def news_view(request):
    news = New.objects.all().order_by("-pub_date")
    latest_news = news.first()  # Получаем последнюю новость
    return render(request, "main/news.html", {"news": news, "latest_news": latest_news})


def new_detail_view(request, id):
    article = get_object_or_404(New, id=id)  # Получаем новость по ID
    images = article.images.all()  # Получаем все изображения для этой новости
    return render(
        request, "main/news_detail.html", {"article": article, "images": images}
    )
