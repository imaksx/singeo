from content.models import AboutIndex


def about_index_processor(request):
    about_index = AboutIndex.objects.first()
    return {"about_index": about_index}
