import csv
import os
import sys

import django
from content.models import IndustryTag

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()


def check_if_industries_exist():
    return IndustryTag.objects.exists()


def create_industries_from_csv():
    if check_if_industries_exist():
        print("Теги отраслей уже существуют. Завершение работы.")
        return

    csv_file_path = os.path.join(BASE_DIR, "industries.csv")

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                IndustryTag.objects.create(name=row["name"], slug=row["slug"])
                print(f"Отрасль '{row['name']}' успешно создана")
            except Exception as e:
                print(f"Ошибка при создании отрасли '{row['name']}': {str(e)}")


if __name__ == "__main__":
    print("Проверка наличия тегов отраслей...")
    if not check_if_industries_exist():
        print("Начинаем загрузку тегов отраслей...")
        create_industries_from_csv()
    else:
        print("Теги отраслей уже существуют в БД.")
    print("Завершение работы.")
