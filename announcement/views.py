from django.shortcuts import render

# Create your views here.

def annoucment(request):
    return render(request,
                  'announcement/announcement.html'
    )
