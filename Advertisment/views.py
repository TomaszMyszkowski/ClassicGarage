from django.shortcuts import render, redirect
from .models import car
from Advertisment.models import car_adveritsment
# Create your views here.
from Advertisment.models import part_of_car_advertisment
from Advertisment.forms import Car_advert


def show_car(request):
    return render(request,
                  'carad/newAd.html'
                  )


def car_adver_add(request):
    if request.method == "POST":
        if request.POST.get('brand') and \
                request.POST.get('model') and \
                request.POST.get('year') and \
                request.POST.get('add_date') and \
                request.POST.get('modified_date') and \
                request.POST.get('end_date') and \
                request.POST.get('prize') and \
                request.POST.get('status') and \
                request.POST.get('location') and \
                request.POST.get('telephone') and \
                request.POST.get('model') and \
                request.POST.get('model'):
            auto = car_adveritsment()
            auto.brand = request.POST.get('brand')
            auto.model = request.POST.get('model')
            auto.year = request.POST.get('year')
            auto.add_date = request.POST.get('add_date')
            auto.modified_date = request.POST.get('modified_date')
            auto.end_date = request.POST.get('end_date')
            auto.prize = request.POST.get('prize')
            auto.status = request.POST.get('status')
            auto.location = request.POST.get('location')
            auto.telephone = request.POST.get('telephone')
            auto.description = request.POST.get('description')
            auto.save()
        return redirect('home')


def parts_adver_add(request):
    if request.method == "POST":
        if request.POST.get('name') and \
                request.POST.get('add_date') and \
                request.POST.get('modified_date') and \
                request.POST.get('end_date') and \
                request.POST.get('prize') and \
                request.POST.get('status') and \
                request.POST.get('location') and \
                request.POST.get('telephone') and \
                request.POST.get('derscription'):
            part = part_of_car_advertisment
            part.brand = request.POST.get('brand')
            part.model = request.POST.get('model')
            part.year = request.POST.get('year')
            part.add_date = request.POST.get('add_date')
            part.modified_date = request.POST.get('modified_date')
            part.end_date = request.POST.get('end_date')
            part.prize = request.POST.get('prize')
            part.status = request.POST.get('status')
            part.location = request.POST.get('location')
            part.telephone = request.POST.get('telephone')
            part.description = request.POST.get('description')
            part.save()
        return redirect('home')


def car_advert1(request):
    form = Car_advert(request.Post or None)
    if form.is_valid():
        form.save()
        return redirect('carad/test.html')

    return render(request,
                  'carad/test.html',
                  context={
                      'form': form
                  })
