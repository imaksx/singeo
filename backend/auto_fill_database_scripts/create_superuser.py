import os
import sys

import django
from django.contrib.auth.models import User
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()


def create_superuser(username, email, password):
    if User.objects.filter(username=username).exists():
        print("Суперпользователь уже существует")
    else:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        print("Суперпользователь успешно создан")


if __name__ == "__main__":
    if not all([ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD]):
        print("Ошибка: не все переменные окружения заданы!")
        sys.exit(1)

    create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
