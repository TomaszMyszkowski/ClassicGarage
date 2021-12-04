from django.shortcuts import render, redirect
from .models import car
# Create your views here.


def show_car(request):
    auto = car.objects.all()
    return render (request,
                   'car.html',
                   {'auto': auto})


def car_add(request):
    if request.method == "POST":
        if request.POST.get('brand') and request.POST.get('model'):
            auto = car()
            auto.brand = request.POST.get('brand')
            auto.model = request.POST.get('model')
            auto.save()
        return redirect('showcar')
