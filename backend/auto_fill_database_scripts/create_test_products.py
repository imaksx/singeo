import os
import sys
import django
import csv
from django.core.files import File
from django.core.files.base import ContentFile
from content.models import Product

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def check_if_products_exist():
    # Проверяем, есть ли уже продукты в базе данных
    return Product.objects.exists()


def create_products_from_csv():
    if check_if_products_exist():
        print("Продукты уже существуют в базе данных. Завершаем работу скрипта.")
        return

    csv_file_path = os.path.join(BASE_DIR, "test_products.csv")

    with open(csv_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Загружаем изображение
            image_path = os.path.join(
                BASE_DIR, "../static/media/products_images/product.png"
            )
            with open(image_path, "rb") as image_file:
                image_content = ContentFile(image_file.read())

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
                print(f"Продукт '{product.name}' успешно создан")
            except Exception as e:
                print(f"Ошибка при создании продукта '{product.name}': {str(e)}")


if __name__ == "__main__":
    print("Начинаем проверку наличия продуктов...")
    if not check_if_products_exist():
        print("Продукты не найдены. Начинаем создание...")
        create_products_from_csv()
    else:
        print("Продукты уже существуют в базе данных. Завершаем работу.")
    print("Процесс завершен")
