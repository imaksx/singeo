def format_multiline_text(text):
    """
    Форматирует текст, разделяя его на список строк по символам \n.

    :param text: Исходный текст с символами \n
    :return: Список строк, разделенных по символам \n
    """
    if text:
        return text.split("\n")  # Разделяем текст на список строк по символам \n
    return []


def get_plural_form(number, form1, form2, form5):
    """Более надёжная реализация склонения для русского языка"""
    try:
        n = abs(int(number))
    except (TypeError, ValueError):
        return form5

    if n % 100 in (11, 12, 13, 14):
        return form5

    remainder = n % 10
    if remainder == 1:
        return form1
    elif 2 <= remainder <= 4:
        return form2
    else:
        return form5
