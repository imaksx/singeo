import csv
import os
import sys

import django
from content.models import Region

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def check_if_regions_exist():
    return Region.objects.exists()


def create_regions_from_csv():
    if check_if_regions_exist():
        print("Регионы уже существуют в базе данных. Завершаем работу скрипта.")
        return

    csv_file_path = os.path.join(BASE_DIR, "regions_percent.csv")

    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            region = Region(
                name=row["name"],
                coord_x=float(row["coord_x"]),
                coord_y=float(row["coord_y"]),
                is_active=False,
            )

            try:
                region.save()
                print(f"Регион '{region.name}' создан (скрыт на карте)")
            except Exception as e:
                print(f"Ошибка при создании региона '{region.name}': {str(e)}")


if __name__ == "__main__":
    print("Начинаем проверку наличия регионов...")
    if not check_if_regions_exist():
        print(
            "Регионы не найдены. Начинаем создание...",
        )
        create_regions_from_csv()
    else:
        print("Регионы уже существуют в базе данных. Завершаем работу.")
    print("Процесс завершен")
