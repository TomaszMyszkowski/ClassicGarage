from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from CarService.forms import ServiceAdvert
from CarAdvertisment.models import ServiceAdvertisment

def servadd(request, id):
    sc = get_object_or_404(ServiceAdvertisment, id=id)
    return render(request,
                  'advertservice.html',
                  context={
                      'sc': sc
                  }
                  )

def service_add(request):

    form = ServiceAdvert((request.POST or None))
    if form.is_valid():
        form.save()
        advert_id = ServiceAdvertisment.objects.order_by("id").last().id
        return redirect('serviceadvert', id=advert_id)
    return render(request,
                  'service-add.html',
                  context={
                      'form': form
                  }
                  )