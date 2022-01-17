from django import forms

from CarAdvertisment.models import ServiceAdvertisment


class ServiceAdvert(forms.ModelForm):
    class Meta:
        model = ServiceAdvertisment
        fields = '__all__'