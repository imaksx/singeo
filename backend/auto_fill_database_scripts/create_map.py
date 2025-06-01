import os
import sys
from django.db import models
import django

# Определяем базовый путь к проекту
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Добавляем путь к родительской директории
sys.path.append(os.path.join(BASE_DIR, ".."))

# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()

from content.models import Map  # Импортируем модель Map


def create_map():
    # Проверяем существование записи
    if Map.objects.exists():
        print("Модель Map уже создана")
    else:
        # Создаем новую запись
        Map.objects.create()
        print("Модель Map успешно создана")


if __name__ == "__main__":
    create_map()
