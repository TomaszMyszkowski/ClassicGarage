
from CarAdvertisment.models import car, CarAdveritsment, PartOfCarAdvertisment, ServiceAdvertisment
from django.contrib import admin
from django.urls import path

from register import views as vr
from home import views as vh
from login import views as vl
from CarAdvertisment import views as vCA
from PartsAdvertisment import views as vPA
admin.site.register(car)
admin.site.register(CarAdveritsment)
admin.site.register(PartOfCarAdvertisment)
admin.site.register(ServiceAdvertisment)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', vr.register, name="register"),
    path('', vh.home, name="home"),
    path('login/', vl.loginPage, name="login"),
    path('logout/', vl.LogoutUser, name="logout"),
    path('car-add/', vCA.car_add, name="car-add"),
    path('caradvert/<int:id>/', vCA.advert, name="caradvert"),
    path('parts-add/', vPA.part_add, name="part-add"),
    path('partadvert/<int:id>/', vPA.part_advert, name="partadvert"),
    path('list/', vCA.show_all_ad, name="showallad")

]
