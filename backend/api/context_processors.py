# your_app/context_processors.py

from content.models import AboutIndex

def about_index_processor(request):
    about_index = AboutIndex.objects.first()  # Получаем первый объект AboutIndex
    return {
        'about_index': about_index  # Возвращаем объект в контексте
    }