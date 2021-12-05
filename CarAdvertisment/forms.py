from django import forms

from CarAdvertisment.models import CarAdveritsment


class CarAdvert(forms.ModelForm):
    class Meta:
        model = CarAdveritsment
        fields = '__all__'
