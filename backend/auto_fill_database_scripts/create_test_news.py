import os
import sys
import django
import csv
from django.core.files.base import ContentFile
from django.db import transaction
from datetime import datetime
from content.models import New, NewsImage

# Определяем базовый путь к проекту
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Добавляем путь к родительской директории
sys.path.append(os.path.join(BASE_DIR, ".."))

# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()

def check_if_news_exist():
    return New.objects.exists()

def create_news_from_csv():
    if check_if_news_exist():
        print("Новости уже существуют в базе данных. Завершаем работу скрипта.")
        return

    # Путь к CSV-файлу
    csv_file_path = os.path.join(BASE_DIR, "news.csv")
    
    # Проверяем существование файла
    if not os.path.exists(csv_file_path):
        print(f"Файл {csv_file_path} не найден!")
        print(f"Список файлов в директории: {os.listdir(os.path.dirname(csv_file_path))}")
        return

    # Пути к медиафайлам
    default_image_path = os.path.join(BASE_DIR, "../static/media/news_images/test_news_image.png")
    video_path = os.path.join(BASE_DIR, "../static/media/news_videos/test_news_video.mp4")
    
    # Проверяем существование файлов
    if not os.path.exists(default_image_path):
        print(f"Изображение по умолчанию не найдено: {default_image_path}")
        return

    try:
        # Читаем изображение один раз для всех новостей
        with open(default_image_path, "rb") as image_file:
            image_content = ContentFile(image_file.read())
            image_name = os.path.basename(default_image_path)

        # Читаем видео (только для первой новости)
        video_content = None
        if os.path.exists(video_path):
            with open(video_path, "rb") as video_file:
                video_content = ContentFile(video_file.read())
                video_name = os.path.basename(video_path)

        with transaction.atomic():
            with open(csv_file_path, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    try:
                        # Преобразуем дату из строки в объект date
                        pub_date = datetime.strptime(row["pub_date"], "%Y-%m-%d").date()
                        
                        news_item = New(
                            name=row["name"],
                            pub_date=pub_date,
                            text=row["text"],
                        )
                        
                        # Добавляем видео только для первой новости
                        if row["id"] == "1" and video_content:
                            news_item.video.save(video_name, ContentFile(video_content.read()))
                            video_content.seek(0)
                        
                        news_item.save()
                        
                        # Добавляем изображение к новости
                        news_image = NewsImage(news=news_item)
                        news_image.image.save(image_name, ContentFile(image_content.read()))
                        news_image.save()
                        
                        print(f"Новость '{news_item.name}' успешно создана")
                        
                        # Сбрасываем указатель файла изображения
                        image_content.seek(0)
                        
                    except Exception as e:
                        print(f"Ошибка при создании новости '{row['name']}': {str(e)}")
    
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
    print("Проверка наличия новостей...")
    if not check_if_news_exist():
        print("Начинаем импорт новостей...")
        create_news_from_csv()
    else:
        print("Новости уже существуют. Импорт не требуется.")
    print("Завершение работы скрипта")