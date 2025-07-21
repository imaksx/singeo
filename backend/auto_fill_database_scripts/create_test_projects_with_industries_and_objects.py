import csv
import os
import random
import sys

import django
from content.models import Product, Project, Region
from django.core.files.base import ContentFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def clear_existing_projects():
    """Удаляет все существующие проекты"""
    if Project.objects.exists():
        print("Удаление существующих проектов...")
        Project.objects.all().delete()
        print("Все существующие проекты удалены")
    else:
        print("Нет существующих проектов для удаления")


def get_random_region():
    """Возвращает случайный регион"""
    regions = list(Region.objects.all())
    if not regions:
        print("Предупреждение: Нет регионов в базе данных!")
        return None
    return random.choice(regions)


def get_random_product():
    """Возвращает случайный продукт"""
    products = list(Product.objects.all())
    if not products:
        print("Предупреждение: Нет продуктов в базе данных!")
        return None
    return random.choice(products)


def create_projects_from_csv():
    if not Region.objects.exists():
        print("Ошибка: Нет регионов в базе данных!")
        return

    if not Product.objects.exists():
        print("Ошибка: Нет продуктов в базе данных!")
        return

    csv_file_path = os.path.join(BASE_DIR, "test_projects.csv")

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            image_path = os.path.join(
                BASE_DIR, "../static/media/projects_images/project.jpg"
            )
            if os.path.exists(image_path):
                with open(image_path, "rb") as image_file:
                    image_content = ContentFile(image_file.read())
            else:
                print(f"Ошибка: Файл изображения не найден: {image_path}")
                image_content = None

            project = Project(
                name=row["name"],
                description=row["description"],
            )

            try:
                if image_content:
                    project.image.save("project.jpg", image_content)
                else:
                    project.save()

                region = get_random_region()
                if region:
                    project.regions.add(region)
                    project.location = region.name
                    print(f"Назначен регион: {region.name} (записано в location)")
                    region.is_active = True
                    region.save()
                    print(f"Регион '{region.name}' активирован (is_active=True)")

                product = get_random_product()
                if product:
                    project.related_products.add(product)
                    print(f"Назначен продукт: {product.name}")
                    industries = product.industries.all()
                    
                    if industries:
                        project.tag_sphere.add(*industries)
                        print(f"Назначены отрасли: {[i.name for i in industries]}")

                    objects = product.applying_objects.all()

                    if objects:
                        project.tag_object.add(*objects)
                        print(f"Назначены объекты: {[o.name for o in objects]}")

                project.save()

                print(f"Проект '{project.name}' успешно создан с ID {project.id}")

            except Exception as e:
                print(f"Ошибка при создании проекта '{row['name']}': {str(e)}")


if __name__ == "__main__":
    print("Начинаем создание проектов...")
    clear_existing_projects()
    create_projects_from_csv()
    print("Процесс завершен")
