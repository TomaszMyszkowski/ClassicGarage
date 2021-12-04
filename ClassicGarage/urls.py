"""ClassicGarage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from CarAdvertisment.models import car, car_adveritsment, part_of_car_advertisment, service_avertisment
from django.contrib import admin
from django.urls import path

from register import views as vr
from home import views as vh
from login import views as vl
from CarAdvertisment import views as vCA

admin.site.register(car)
admin.site.register(car_adveritsment)
admin.site.register(part_of_car_advertisment)
admin.site.register(service_avertisment)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', vr.register, name="register"),
    path('', vh.home, name="home"),
    path('login/', vl.loginPage, name="login"),
    path('logout/', vl.LogoutUser, name="logout"),
    path('car',vCA.show_car, name="showcar"),
    path('carad/', vCA.car_add, name="caradd")




]
