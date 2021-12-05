from django.shortcuts import render, redirect, get_object_or_404
from PartsAdvertisment.forms import PartsAdvert
from CarAdvertisment.models import PartOfCarAdvertisment

# Create your views here.

def part_add(request):

    form = PartsAdvert(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('advert')
    return render(request,
                  'part-add.html',
                  context={
                      'form': form
                  }
                  )

def part_advert(request, user):
    ad = get_object_or_404(PartOfCarAdvertisment, user=user)

    return render(request,
                  'partadvertview.html',
                  context={
                      'ad': ad
                  }
                  )