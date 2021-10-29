from django.forms import ModelForm
from .models import Publication, Conference
from django import forms
from django.forms.fields import CheckboxInput, Select

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class PublicationForm(ModelForm):

    class Meta:

        CHOICES = [('1', 'Первое'), ('2', 'Второе')]

        model = Publication
        # fields = ['kind', 'year', 'halfyear', 'outputdata', 'sheetcount',]

        exclude = ['id_access', 'orgfounders', 'ininternationals', 'authors', 'subdivisions', 'anr']
        widgets = {'forumdate': myDateInput,
                   'scienceworkstudentparticipation': CheckboxInput(),
                   'workisforeignauthors': CheckboxInput(),
                   'halfyear': Select(choices=CHOICES),
                   }


class ConferenceForm(ModelForm):

    class Meta:
        model = Conference
        fields = '__all__'
        widgets = {'forumdate': myDateInput,
                   }
