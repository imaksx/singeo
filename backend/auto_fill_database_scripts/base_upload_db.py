import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    try:
        with open("create_superuser.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open("create_map.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open("create_about_index.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open("create_about_company.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open("create_test_news.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open("create_regions.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open("create_industries.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open("create_objects.py", "r", encoding="utf-8") as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open(
            "create_test_products_with_industries_and_objects.py",
            "r",
            encoding="utf-8",
        ) as file:
            script_content = file.read()
        exec(script_content)
        print("")

        with open(
            "create_test_projects_with_industries_and_objects.py",
            "r",
            encoding="utf-8",
        ) as file:
            script_content = file.read()
        exec(script_content)
        print("")

        print("")
        print("Все скрипты выполнены успешно")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
