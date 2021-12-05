from django.shortcuts import render, redirect
from CarAdvertisment.models import CarAdveritsment
from CarAdvertisment.forms import CarAdvert
from django.shortcuts import get_object_or_404




def advert(request, id):
    ad = get_object_or_404(CarAdveritsment, id=id)
    return render(request,
                  'advertview.html',
                  context={
                      'ad': ad
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

