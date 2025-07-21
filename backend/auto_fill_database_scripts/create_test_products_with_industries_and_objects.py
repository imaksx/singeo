import csv
import os
import random
import sys

import django
from content.models import IndustryTag, ObjectTag, Product
from django.core.files.base import ContentFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()

INDUSTRY_SLUGS = ["oil-and-gas", "energy", "construction"]
OBJECT_SLUGS = ["oil-refinery", "power-plant", "residential-complex"]


def clear_existing_products():
    """Удаляет все существующие продукты"""
    if Product.objects.exists():
        print("Удаление существующих продуктов...")
        Product.objects.all().delete()
        print("Все существующие продукты удалены")
    else:
        print("Нет существующих продуктов для удаления")


def get_industry_by_slug(slug):
    """Возвращает отрасль по slug или None если не найдена"""
    try:
        return IndustryTag.objects.get(slug=slug)
    except IndustryTag.DoesNotExist:
        print(f"Предупреждение: Отрасль со slug '{slug}' не найдена!")
        return None


def get_object_by_slug(slug):
    """Возвращает объект по slug или None если не найдена"""
    try:
        return ObjectTag.objects.get(slug=slug)
    except ObjectTag.DoesNotExist:
        print(f"Предупреждение: Объект со slug '{slug}' не найден!")
        return None


def get_random_industries():
    """Возвращает 1-3 случайные отрасли по их slug"""
    selected_slugs = random.sample(
        INDUSTRY_SLUGS, k=random.randint(1, min(3, len(INDUSTRY_SLUGS)))
    )
    industries = []
    for slug in selected_slugs:
        industry = get_industry_by_slug(slug)
        if industry:
            industries.append(industry)
    return industries


def get_random_objects():
    """Возвращает 1-3 случайных объекта применения по их slug"""
    selected_slugs = random.sample(
        OBJECT_SLUGS, k=random.randint(1, min(3, len(OBJECT_SLUGS)))
    )
    objects = []
    for slug in selected_slugs:
        obj = get_object_by_slug(slug)
        if obj:
            objects.append(obj)
    return objects


def create_products_from_csv():
    print(
        "Доступные отрасли:",
        list(
            IndustryTag.objects.values_list(
                "slug",
                flat=True,
            )
        ),
    )
    print(
        "Доступные объекты:",
        list(
            ObjectTag.objects.values_list(
                "slug",
                flat=True,
            )
        ),
    )

    csv_file_path = os.path.join(BASE_DIR, "test_products.csv")

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            image_path = os.path.join(
                BASE_DIR, "../static/media/products_images/product.png"
            )
            if os.path.exists(image_path):
                with open(image_path, "rb") as image_file:
                    image_content = ContentFile(image_file.read())
            else:
                print(f"Ошибка: Файл изображения не найден: {image_path}")
                image_content = None

            product = Product(
                name=row["name"],
                short_description=row["short_description"],
                description=row["description"],
                specifications=row["specifications"],
            )

            try:
                if image_content:
                    product.preview.save("product.png", image_content)
                else:
                    product.save()

                industries = get_random_industries()
                if industries:
                    product.industries.set(industries)
                    print(f"Назначены отрасли: {[i.slug for i in industries]}")
                else:
                    print("Не удалось назначить отрасли - ни одна не найдена")

                applying_objects = get_random_objects()
                if applying_objects:
                    product.applying_objects.set(applying_objects)
                    print(f"Назначены объекты: {[o.slug for o in applying_objects]}")
                else:
                    print("Не удалось назначить объекты - ни один не найден")

                product.save()

                print(f"Продукт '{product.name}' успешно создан с ID {product.id}")

            except Exception as e:
                print(f"Ошибка при создании продукта '{row['name']}': {str(e)}")


if __name__ == "__main__":
    print("Начинаем создание продуктов...")
    clear_existing_products()
    create_products_from_csv()
    print("Процесс завершен")
