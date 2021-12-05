from django.shortcuts import render, redirect
from .models import car
from CarAdvertisment.models import car_adveritsment
from CarAdvertisment.forms import CarAdvert
# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User



def advert(request, user):
    ad = get_object_or_404(car_adveritsment, user=user)

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
        return redirect('advert')
    return render(request,
                  'car-add.html',
                  context={
                      'form': form
                  }
                  )

