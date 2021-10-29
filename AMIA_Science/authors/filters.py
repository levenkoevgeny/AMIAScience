import django_filters
from .models import Author, Subdivision, Position, Candidatespecialty, Doctorspecialty, Rank
from django import forms


class AuthorFilter(django_filters.FilterSet):

    DOCENT_VAK_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )

    subdivision = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    lastname = django_filters.CharFilter(field_name='lastname', lookup_expr='icontains')
    isdocentvak = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)
    isprofessor = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)
    iscandidate = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)
    isdoctor = django_filters.ChoiceFilter(choices=DOCENT_VAK_CHOICES, widget=forms.Select)

    docentvakdate_gte = django_filters.NumberFilter(field_name='docentvakdate__year', lookup_expr='gte')
    docentvakdate_lte = django_filters.NumberFilter(field_name='docentvakdate__year', lookup_expr='lte')
    professordate_gte = django_filters.NumberFilter(field_name='professordate__year', lookup_expr='gte')
    professordate_lte = django_filters.NumberFilter(field_name='professordate__year', lookup_expr='lte')
    candidatedate_gte = django_filters.NumberFilter(field_name='candidatedate__year', lookup_expr='gte')
    candidatedate_lte = django_filters.NumberFilter(field_name='candidatedate__year', lookup_expr='lte')
    doctordate_gte = django_filters.NumberFilter(field_name='doctordate__year', lookup_expr='gte')
    doctordate_lte = django_filters.NumberFilter(field_name='doctordate__year', lookup_expr='lte')

    class Meta:
        model = Author
        fields = [
            'rank',
            'position',
            'doctorspecialty'
        ]
