import os
import sys

import django
from content.models import Map

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(BASE_DIR, ".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def create_map():
    if Map.objects.exists():
        print("Модель Map уже создана")
    else:
        Map.objects.create()
        print("Модель Map успешно создана")


if __name__ == "__main__":
    create_map()
