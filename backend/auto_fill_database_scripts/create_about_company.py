import csv
import os
import sys

import django
from content.models import AboutCompany, Colleague
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def create_about_company():
    if AboutCompany.objects.exists():
        print("Модель AboutCompany уже создана")
        return

    if not os.path.exists("about_company.csv"):
        print("Файл about_company.csv не найден в текущем каталоге")
        print(f"Список файлов в текущем каталоге: {os.listdir()}")
        return

    try:
        with open(
            "about_company.csv",
            newline="",
            encoding="utf-8",
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            row = next(reader)

            image_path = row["colleagues_main_image"]
            if image_path:
                with open(image_path, "rb") as image_file:
                    image_content = ContentFile(image_file.read())
                    image_name = os.path.basename(image_path)
                    image_path = default_storage.save(
                        f"company_image/{image_name}", image_content
                    )
            else:
                image_path = None

            company = AboutCompany.objects.create(
                company_description=row["company_description"],
                colleagues_description=row["colleagues_description"],
                colleagues_main_image=image_path,
            )

            if row["colleagues"]:
                colleague_ids = row["colleagues"].split(",")
                for colleague_id in colleague_ids:
                    try:
                        colleague = Colleague.objects.get(id=int(colleague_id))
                        company.colleagues.add(colleague)
                    except Colleague.DoesNotExist:
                        print(f"Коллега с ID {colleague_id} не найден")

            print("Модель AboutCompany успешно создана")

    except FileNotFoundError:
        print("Файл about_company.csv не найден")
    except Exception as e:
        print(f"Ошибка при создании модели: {str(e)}")


if __name__ == "__main__":
    create_about_company()
