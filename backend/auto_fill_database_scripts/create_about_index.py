import os
import sys
import django
import csv

from content.models import AboutIndex

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def create_about_index():
    if AboutIndex.objects.exists():
        print("Модель AboutIndex уже создана")
        return

    try:
        with open("about_index.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            row = next(reader)

            AboutIndex.objects.create(
                phone=row["phone"],
                email=row["email"],
                address=row["address"],
                slogan=row["slogan"],
                description_1=row["description_1"],
                description_2=row["description_2"],
            )
            print("Модель AboutIndex успешно создана")

    except FileNotFoundError:
        print("Файл about_index.csv не найден")
    except Exception as e:
        print(f"Ошибка при создании модели: {str(e)}")


if __name__ == "__main__":
    create_about_index()
