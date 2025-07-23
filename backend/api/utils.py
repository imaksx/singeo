def format_multiline_text(text):
    """
    Форматирует текст, разделяя его на список строк по символам \n.
    
    :param text: Исходный текст с символами \n
    :return: Список строк, разделенных по символам \n
    """
    if text:
        return text.split('\n')  # Разделяем текст на список строк по символам \n
    return []

def get_plural_form(number, form1, form2, form5):
    """
    Возвращает правильную форму слова для числа по правилам русского языка.
    form1: 1, 21, 31... (но не 11, 111)
    form2: 2-4, 22-24... (но не 12-14)
    form5: 5-20, 25-30, 11-14...
    """
    n = abs(number) % 100
    n1 = n % 10
    
    if 10 < n < 20:
        return form5
    elif 1 < n1 < 5:
        return form2
    elif n1 == 1:
        return form1
    return form5