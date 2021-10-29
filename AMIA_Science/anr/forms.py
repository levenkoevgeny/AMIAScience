from django.forms import ModelForm
from .models import ANR
from django import forms
from django.forms.fields import CheckboxInput, Select

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class ANRForm(ModelForm):

    class Meta:

        CHOICES = [('1', 'Первое'), ('2', 'Второе')]

        model = ANR
        exclude = ['id_access', 'subdivisions',]
        widgets = {'approvedate': myDateInput,
                   'is_student_participation': CheckboxInput(),
                   'development_has_not_base': CheckboxInput(),
                   'halfyear': Select(choices=CHOICES),
                   }
