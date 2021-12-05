from django.shortcuts import render, redirect

# Create your views here.
from CarService.forms import ServiceAdvert
from CarAdvertisment.models import ServiceAdvertisment

def advert(request, id):
    ad = get_object_or_404(ServiceAdvertisment, id=id)
    return render(request,
                  'advertview.html',
                  context={
                      'ad': ad
                  }
                  )

def car_add(request):

    form = ServiceAdvert((request.POST or None))
    if form.is_valid():
        form.save()
        advert_id = ServiceAdvertisment.objects.order_by("id").last().id
        return redirect('caradvert', id=advert_id)
    return render(request,
                  'service-add.html',
                  context={
                      'form': form
                  }
                  )