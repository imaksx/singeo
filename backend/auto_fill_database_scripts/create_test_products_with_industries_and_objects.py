import os
import sys
import django
import csv
import random
from django.core.files import File
from django.core.files.base import ContentFile
from content.models import Product, IndustryTag, ObjectTag

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def check_if_products_exist():
    return Product.objects.exists()


def get_random_industries():
    """Возвращает 1-3 случайные отрасли"""
    industries = list(IndustryTag.objects.all())
    if not industries:
        print("Предупреждение: Нет отраслей в базе данных!")
        return []
    return random.sample(industries, k=min(random.randint(1, 3), len(industries)))


def get_random_objects():
    """Возвращает 1-3 случайных объекта применения"""
    objects = list(ObjectTag.objects.all())
    if not objects:
        print("Предупреждение: Нет объектов применения в базе данных!")
        return []
    return random.sample(objects, k=min(random.randint(1, 3), len(objects)))


def create_products_from_csv():
    if check_if_products_exist():
        print("Продукты уже существуют в базе данных. Завершаем работу скрипта.")
        return

    # Проверяем наличие тегов
    industries_count = IndustryTag.objects.count()
    objects_count = ObjectTag.objects.count()
    print(f"Найдено отраслей: {industries_count}, объектов применения: {objects_count}")

    csv_file_path = os.path.join(BASE_DIR, "test_products.csv")

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Загружаем изображение
            image_path = os.path.join(
                BASE_DIR, "../static/media/products_images/product.png"
            )
            with open(image_path, "rb") as image_file:
                image_content = ContentFile(image_file.read())

            # Создаем продукт
            product = Product(
                name=row["name"],
                short_description=row["short_description"],
                description=row["description"],
                specifications=row["specifications"],
            )

            # Устанавливаем изображение
            product.preview.save("product.png", image_content)

            try:
                product.save()

                # Добавляем случайные отрасли (если они есть)
                industries = get_random_industries()
                if industries:
                    product.industries.set(industries)  # Исправлено на industries

                # Добавляем случайные объекты применения (если они есть)
                applying_objects = get_random_objects()
                if applying_objects:
                    product.applying_objects.set(applying_objects)

                print(
                    f"Продукт '{product.name}' создан. "
                    f"Отрасли: {[i.name for i in industries] if industries else 'нет'}, "
                    f"Объекты: {[o.name for o in applying_objects] if applying_objects else 'нет'}"
                )

            except Exception as e:
                print(f"Ошибка при создании продукта '{row['name']}': {str(e)}")


if __name__ == "__main__":
    print("Начинаем проверку наличия продуктов...")
    if not check_if_products_exist():
        print("Продукты не найдены. Начинаем создание...")
        create_products_from_csv()
    else:
        print("Продукты уже существуют в базе данных. Завершаем работу.")
    print("Процесс завершен")