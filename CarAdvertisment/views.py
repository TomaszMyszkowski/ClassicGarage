from django.shortcuts import render
from .models import car
# Create your views here.


def show_car(request):
    auto = car.objects.all()
    return render (request,
                   'car.html',
                   {'auto':auto})


def car_add(request):
    if request.method == "POST":
        brand = request.POST.get('brand')
        if brand:
            car.objects.create(brand=brand)





    return render(
        request,
        'car.html',
    )

