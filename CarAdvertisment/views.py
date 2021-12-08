from django.shortcuts import render, redirect, get_list_or_404
from CarAdvertisment.models import CarAdveritsment
from CarAdvertisment.forms import CarAdvert
from django.shortcuts import get_object_or_404




def advert(request, id):
    advert = get_object_or_404(CarAdveritsment, id=id)
    return render(request,
                  'advertview.html',
                  context={
                      'advert': advert
                  }
                  )


def car_add(request):

    form = CarAdvert(request.POST or None)
    if form.is_valid():
        form.save()
        advert_id = CarAdveritsment.objects.order_by("id").last().id
        return redirect('caradvert', id=advert_id)
    return render(request,
                  'car-add.html',
                  context={
                      'form': form
                  }
                  )

def show_all_ad(request):
    allad = get_list_or_404(CarAdveritsment)
    return render(request,
                  'list.html',
                  context={
                      'allad':allad
                  }

                  )