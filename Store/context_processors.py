from Store.models import *


def categories(request):
    return {
        'categories': Category.objects.all()
    }