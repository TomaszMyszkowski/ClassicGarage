from django import forms
from models import car

class carmodel(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = car
        fields = [
            'brand',
            'model',
        ]

