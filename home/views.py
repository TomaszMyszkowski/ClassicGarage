from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.


from CarAdvertisment.models import ServiceAdvertisment


def home(request):
    adverts = ServiceAdvertisment.objects.all()
    paginator = Paginator(adverts, 5)

    page_num = request.GET.get('page')

    page = paginator.get_page(page_num)
    context = {
        'count': paginator.count,
        'page': page
    }
    return render(request, 'home/new_home.html', context)

# def home(request):
#     return render(
#         request,
#         "home/home.html"
#     )