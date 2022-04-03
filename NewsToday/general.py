from . models import Category

def globals(request):
    content = {
        'categoryData': Category.objects.all()
    }
    return content