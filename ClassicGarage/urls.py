
from CarAdvertisment.models import car, car_adveritsment, part_of_car_advertisment, service_advertisment
from django.contrib import admin
from django.urls import path

from register import views as vr
from home import views as vh
from login import views as vl
from CarAdvertisment import views as vCA

admin.site.register(car)
admin.site.register(car_adveritsment)
admin.site.register(part_of_car_advertisment)
admin.site.register(service_advertisment)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', vr.register, name="register"),
    path('', vh.home, name="home"),
    path('login/', vl.loginPage, name="login"),
    path('logout/', vl.LogoutUser, name="logout"),
    path('car-add/', vCA.car_add, name="car-add"),
    path('advert/<str:user>/', vCA.advert, name="advert")

]
