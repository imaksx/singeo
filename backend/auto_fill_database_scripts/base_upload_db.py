import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    try:
        # Запуск create_superuser.py
        with open("create_superuser.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)

        # Запуск create_map.py
        with open("create_map.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)

        print("Все скрипты выполнены успешно")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
