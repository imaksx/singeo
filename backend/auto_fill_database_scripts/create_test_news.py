import os
import sys
import django
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import transaction
from datetime import datetime as dt

from content.models import New, NewsImage

# Определяем базовый путь к проекту
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Добавляем путь к родительской директории
sys.path.append(os.path.join(BASE_DIR, ".."))

# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def create_news():
    # Проверяем существование записей
    if New.objects.exists():
        print("Новости уже созданы")
        return

    # Проверяем существование файла
    if not os.path.exists("news.csv"):
        print("Файл news.csv не найден в текущем каталоге")
        print(f"Список файлов в текущем каталоге: {os.listdir()}")
        return

    try:
        with open("news.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            news_data = []

            # Читаем данные
            for row in reader:
                news_data.append(row)

        # Создаем новости
        with transaction.atomic():
            for row in news_data:
                try:
                    pub_date = dt.strptime(row["pub_date"], "%Y-%m-%d").date()
                except ValueError:
                    print(f"Ошибка форматирования даты: {row['pub_date']}")
                    continue

                news = New(name=row["name"], pub_date=pub_date, text=row["text"])

                # Загружаем видео, если оно есть
                if row["video"]:
                    video_path = row["video"]
                    if os.path.exists(video_path):
                        with open(video_path, "rb") as video_file:
                            video_content = ContentFile(video_file.read())
                            video_name = os.path.basename(video_path)
                            news.video.save(video_name, video_content)
                    else:
                        print(f"Видеофайл не найден: {video_path}")

                # Сохраняем новость перед загрузкой изображений
                news.save()

                # Загружаем изображение, если оно есть
                if row["image"]:
                    image_path = row["image"]
                    if os.path.exists(image_path):
                        with open(image_path, "rb") as image_file:
                            image_content = ContentFile(image_file.read())
                            image_name = os.path.basename(image_path)
                            news_image = NewsImage(news=news)
                            news_image.image.save(image_name, image_content)
                    else:
                        print(f"Изображение не найдено: {image_path}")

        print("Новости успешно созданы")

    except FileNotFoundError:
        print("Файл news.csv не найден")
    except Exception as e:
        print(f"Ошибка при создании новостей: {str(e)}")


if __name__ == "__main__":
    create_news()
