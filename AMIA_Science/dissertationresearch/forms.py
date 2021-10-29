from django.forms import ModelForm
from .models import Dissertationresearch
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class DissertationResearchForm(ModelForm):

    class Meta:
        model = Dissertationresearch
        exclude = ['leadersemployeessubdivision']
        widgets = {
            'dateprotect': myDateInput,
        }