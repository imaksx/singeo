# Инструкция по развёртыванию проекта singeo (backend)

## 1. Клонирование репозитория

```bash
git clone <URL_репозитория>
cd singeo_project/singeo/backend
```

## 2. Создание и активация виртуального окружения

Требуется Python 3.9+.

```bash
python -m venv venv
source venv/Scripts/activate      # Git Bash / MSYS (UCRT64) на Windows
```

Для PowerShell: `venv\Scripts\activate`, для cmd: `venv\Scripts\activate.bat`.

Активация считается успешной, если в строке терминала появился префикс `(venv)`.

## 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

Если файла `requirements.txt` нет — установить Django вручную:

```bash
pip install django
```

Проверка: `python -m pip list` — в списке должен быть Django.

## 4. Настройка окружения (.env)

Если в репозитории есть `env.example` или шаблон `.env`:

```bash
cp env.example .env
```

Заполните переменные (секретный ключ Django, параметры подключения к базе данных и т.д.). Без `.env` проект может не запуститься.

## 5. Применение миграций

Из папки `backend` (где лежит `manage.py`):

```bash
python manage.py migrate
```

## 6. Запуск скриптов наполнения БД

Скрипты лежат в `backend/auto_fill_database_scripts/`.

**Важно:** в начале файла `base_upload_db.py` должна быть инициализация Django
(иначе возникает ошибка `Requested setting INSTALLED_APPS, but settings are not configured`):

```python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'singeo_backend.settings')

# папка с manage.py — на уровень выше папки со скриптами
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

django.setup()

if __name__ == "__main__":
    ...
```

Запуск — из папки `auto_fill_database_scripts` (скрипты открывают файлы по
относительному пути, поэтому рабочая директория важна):

```bash
cd auto_fill_database_scripts
python base_upload_db.py
```

В конце должно появиться: `Все скрипты выполнены успешно`.

Скрипт последовательно выполняет: создание суперпользователя, карты,
страниц «О компании», тестовых новостей, регионов, отраслей, объектов,
тестовых товаров и проектов.

**Возможная ошибка:** `NameError: name '__file__' is not defined` — возникает,
если запускать скрипт через `python manage.py shell < base_upload_db.py`.
Запускайте напрямую: `python base_upload_db.py`.

## 7. Создание суперпользователя (если не создался скриптом)

```bash
cd ..
python manage.py createsuperuser
```

## 8. Запуск проекта на локальной машине

```bash
python manage.py runserver
```

Сервер будет доступен по адресу: http://127.0.0.1:8000
Админ-панель: http://127.0.0.1:8000/admin

## Типичные проблемы

| Ошибка | Причина | Решение |
|---|---|---|
| `ModuleNotFoundError: No module named 'django'` | Окружение не активировано или зависимости не установлены | Активировать venv, выполнить `pip install -r requirements.txt` |
| `settings are not configured` | Скрипт запущен без инициализации Django | Добавить `django.setup()` в начало скрипта (см. раздел 6) |
| `NameError: __file__` | Запуск через `manage.py shell < script` | Запускать `python base_upload_db.py` напрямую |
| Опечатка в команде | `runsever` вместо `runserver` | Проверить написание команды |
