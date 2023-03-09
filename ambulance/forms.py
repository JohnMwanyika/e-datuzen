from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

# Ambulance request form


class AmbulanceRequestForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = ['contact_phone', 'location', 'cartegory', 'description']
        widgets = {
            'contact_phone':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g 07123...'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g Caltex'}),
            'cartegory':forms.TextInput(attrs={'class':'form-select'}),
            'description':forms.TextInput(attrs={'class':'form-control','placeholder':'e.g 2 casualties'})
        }