from django import forms

from CarAdvertisment.models import PartOfCarAdvertisment



class PartsAdvert(forms.ModelForm):
    class Meta:
        model = PartOfCarAdvertisment
        fields = '__all__'
