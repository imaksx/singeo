import os
import sys
import django
import csv
from django.core.files import File
from django.core.files.base import ContentFile
from content.models import ObjectTag  # Убедитесь, что путь к модели правильный

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()


def check_if_objects_exist():
    return ObjectTag.objects.exists()


def create_objects_from_csv():
    if check_if_objects_exist():
        print("Теги объектов уже существуют. Завершение работы.")
        return

    csv_file_path = os.path.join(BASE_DIR, "objects.csv")

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                ObjectTag.objects.create(name=row["name"], slug=row["slug"])
                print(f"Объект '{row['name']}' успешно создан")
            except Exception as e:
                print(f"Ошибка при создании объекта '{row['name']}': {str(e)}")


if __name__ == "__main__":
    print("Проверка наличия тегов объектов...")
    if not check_if_objects_exist():
        print("Начинаем загрузку тегов объектов...")
        create_objects_from_csv()
    else:
        print("Теги объектов уже существуют в БД.")
    print("Завершение работы.")
