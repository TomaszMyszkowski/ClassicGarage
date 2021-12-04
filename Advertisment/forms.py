from django import forms

from Advertisment.models import car_adveritsment


class Car_advertisment1(forms.ModelForm):
    class Meta:
        model = car_adveritsment
        fields = [
            'brand',
            'model',
            'year',
            'add_date',
            'modified_date',
            'end_date',
            'prize',
            'status',
            'location',
            'telephone',
            'description',
        ]

class Car_advert(forms.ModelForm):
    class Meta:
        model = car_adveritsment
        fields = '__all__'