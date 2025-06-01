from dotenv import load_dotenv
import os
import django
import sys

# Указываем полный путь к файлу.env, который находится на уровень выше
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# Получаем значения из окружения
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

# Добавляем путь к родительской директории
sys.path.append("..")

# Устанавливаем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singeo_backend.settings")
django.setup()

from django.contrib.auth.models import User  # Импортируем после настройки Django


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
    # Добавляем проверку на существование переменных
    if not all([ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD]):
        print("Ошибка: не все переменные окружения заданы!")
        sys.exit(1)

    create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
