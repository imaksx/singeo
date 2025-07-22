import os
import zipfile

from content.models import (
    AboutCompany,
    Certificate,
    Colleague,
    IndustryTag,
    New,
    ObjectTag,
    Product,
    Project,
    Region,
)
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

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
                    certificate.image.path,
                    os.path.basename(
                        certificate.image.path,
                    ),
                )

    with open(zip_filepath, "rb") as zip_file:
        response = HttpResponse(zip_file.read(), content_type="application/zip")
        response["Content-Disposition"] = f"attachment; filename={zip_filename}"

    os.remove(zip_filepath)

    return response


def about_company_view(request):
    """Функция для страницы 'О компании'."""

    about_company = AboutCompany.objects.first()
    certificates = Certificate.objects.all()
    established_year = 2020
    current_year = timezone.now().year
    years_in_market = current_year - established_year
    project_count = Project.objects.count()
    logo_images = about_company.logo_images.all()
    company_pdfs = about_company.pdfs.all()
    colleagues = Colleague.objects.all()

    def get_declension(number, forms):
        if not isinstance(number, int):
            return ""
        if 10 <= number % 100 <= 20:
            return forms[2]
        last_digit = number % 10
        if last_digit == 1:
            return forms[0]
        elif 2 <= last_digit <= 4:
            return forms[1]
        else:
            return forms[2]

    try:
        years_text = get_declension(
            years_in_market, 
            ["год на рынке", "года на рынке", "лет на рынке"]
        )
    except Exception as e:
        years_text = f"Ошибка: {str(e)}"

    try:
        projects_text = get_declension(
            project_count, 
            ["действующий проект", "действующих проекта", "действующих проектов"]
        )
    except Exception as e:
        projects_text = f"Ошибка: {str(e)}"
        
    context = {
        "about_company": about_company,
        "colleagues": colleagues,
        "years_in_market": years_in_market,
        "project_count": project_count,
        "years_text": years_text,
        "projects_text": projects_text,
        "certificates": certificates,
        "logo_images": logo_images,
        "company_pdfs": company_pdfs,
    }

    return render(request, "main/about_company.html", context)


def index_view(request):
    """Функция для главной страницы."""

    products = Product.objects.all()
    projects = Project.objects.all()
    regions = (
        Region.objects.filter(is_active=True, projects__isnull=False)
        .distinct()
        .prefetch_related("projects")
    )

    for region in regions:
        region.coords_x = str(region.coord_x).replace(",", ".")
        region.coords_y = str(region.coord_y).replace(",", ".")

    return render(
        request,
        "main/index.html",
        {
            "products": products,
            "projects": projects,
            "regions": regions,
        },
    )


def project_list(request):
    """Функция для страницы со всеми проектами."""

    projects = Project.objects.all()
    object_tags = ObjectTag.objects.all()
    industry_tags = IndustryTag.objects.all()
    products_used_in_projects = Product.objects.filter(
        projectproduct__project__in=projects
    ).distinct()

    context = {
        "projects": projects,
        "object_tags": object_tags,
        "industry_tags": industry_tags,
        "products_used_in_projects": products_used_in_projects,
    }
    return render(request, "main/projects.html", context)


def products_view(request):
    """Функция для страницы со всеми продуктами."""

    products = Product.objects.all()
    return render(request, "main/products.html", {"products": products[:12]})


def product_detail_view(request, id):
    """Функция для отдельной страницы продукта."""

    product = get_object_or_404(Product, id=id)
    related_projects = product.project_set.all()

    return render(
        request,
        "main/product_detail.html",
        {
            "product": product,
            "related_projects": related_projects,
            "specifications": format_multiline_text(product.specifications),
        },
    )


def project_detail_view(request, id):
    """Функция для отдельной страницы проекта."""

    project = get_object_or_404(Project, id=id)
    return render(request, "main/project_detail.html", {"project": project})


def news_view(request):
    """Функция для страницы со всеми новостями."""

    news = New.objects.all().order_by("-pub_date")
    latest_news = news.first()
    return render(
        request,
        "main/news.html",
        {
            "news": news[:12],
            "latest_news": latest_news,
        },
    )


def new_detail_view(request, id):
    """Функция для отдельной страницы новости."""

    article = get_object_or_404(New, id=id)
    images = article.images.all()
    return render(
        request,
        "main/news_detail.html",
        {
            "article": article,
            "images": images,
        },
    )


def news_view_paginator(request, page=1):
    news_list = New.objects.all().order_by("-pub_date")
    news_data = []
    slicer = page * 12
    checker = True

    if (len(news_list) - 1) < (slicer + 12):
        checker = False

    for article in news_list[slicer : (slicer + 12)]:
        image_url = (
            article.images.first().image.url if article.images.exists() else None
        )
        news_data.append(
            {
                "id": article.id,
                "name": article.name,
                "pub_date": article.pub_date.strftime("%d.%m.%Y"),
                "text": article.text[:150] + "..."
                if len(article.text) > 150
                else article.text,
                "image_url": image_url,
                "detail_url": f"/news/{article.id}/",
            }
        )
    return JsonResponse({"news": news_data, "checker": checker})


def product_view_paginator(request, page=1):
    product_list = Product.objects.all()
    product_data = []
    slicer = page * 12
    checker = True

    if (len(product_list) - 1) < (slicer + 12):
        checker = False

    for product in product_list[slicer : (slicer + 12)]:
        image_url = product.preview.url
        product_data.append(
            {
                "name": product.name,
                "short_description": product.short_description,
                "preview": image_url,
                "detail_url": f"/product/{product.id}/",
            }
        )
    return JsonResponse({"products": product_data, "checker": checker})
