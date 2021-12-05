from django import forms

from CarAdvertisment.models import car_adveritsment


class CarAdvert(forms.ModelForm):
    class Meta:
        model = car_adveritsment
        fields = '__all__'
