import os
import sys
import django
import csv
from django.core.files.base import ContentFile
from django.db import transaction
from content.models import Product

# Определяем базовый путь к проекту
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Добавляем путь к родительской директории
sys.path.append(os.path.join(BASE_DIR, ".."))

# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()

def check_if_products_exist():
    return Product.objects.exists()

def create_products_from_csv():
    if check_if_products_exist():
        print("Продукты уже существуют в базе данных. Завершаем работу скрипта.")
        return

    # Путь к CSV-файлу
    csv_file_path = os.path.join(BASE_DIR, "test_products.csv")
    
    # Проверяем существование файла
    if not os.path.exists(csv_file_path):
        print(f"Файл {csv_file_path} не найден!")
        print(f"Список файлов в директории: {os.listdir(os.path.dirname(csv_file_path))}")
        return

    # Путь к изображению по умолчанию
    default_image_path = os.path.join(BASE_DIR, "../static/media/products_images/product.png")
    
    # Проверяем существование изображения
    if not os.path.exists(default_image_path):
        print(f"Изображение по умолчанию не найдено: {default_image_path}")
        return

    try:
        # Читаем изображение один раз для всех продуктов
        with open(default_image_path, "rb") as image_file:
            image_content = ContentFile(image_file.read())
            image_name = os.path.basename(default_image_path)

        with transaction.atomic():
            with open(csv_file_path, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    try:
                        product = Product(
                            name=row["name"],
                            short_description=row["short_description"],
                            description=row["description"],
                            specifications=row["specifications"],
                        )
                        
                        # Создаем копию изображения для каждого продукта
                        product.preview.save(image_name, ContentFile(image_content.read()))
                        product.save()
                        print(f"Продукт '{product.name}' успешно создан")
                        
                        # Сбрасываем указатель файла изображения
                        image_content.seek(0)
                        
                    except Exception as e:
                        print(f"Ошибка при создании продукта '{row['name']}': {str(e)}")
    
    except UnicodeDecodeError:
        # Пробуем альтернативные кодировки
        try:
            with open(csv_file_path, "r", newline="", encoding="cp1251") as csvfile:
                reader = csv.DictReader(csvfile)
                # ... (повторить обработку как выше)
        except Exception as alt_e:
            print(f"Ошибка при чтении CSV в кодировке cp1251: {str(alt_e)}")
    except Exception as e:
        print(f"Общая ошибка: {str(e)}")

if __name__ == "__main__":
    print("Проверка наличия продуктов...")
    if not check_if_products_exist():
        print("Начинаем импорт продуктов...")
        create_products_from_csv()
    else:
        print("Продукты уже существуют. Импорт не требуется.")
    print("Завершение работы скрипта")