import django_filters
from .models import PLD, PatentOwner
from authors.models import Author, Subdivision
from django import forms


class PLD_Filter(django_filters.FilterSet):

    HALFYEAR_CHOICES = (
        (1, 'Первое'),
        (2, 'Второе'),
    )

    BOOLEAN_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )

    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    subdivisions = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    patentowner = django_filters.ModelMultipleChoiceFilter(queryset=PatentOwner.objects.all())
    pldtitle = django_filters.CharFilter(lookup_expr='icontains')
    actionstart_gte = django_filters.NumberFilter(field_name='actionstart__year', lookup_expr='gte')
    actionstart_lte = django_filters.NumberFilter(field_name='actionstart__year', lookup_expr='lte')
    registrationdate_gte = django_filters.NumberFilter(field_name='registrationdate__year', lookup_expr='gte')
    registrationdate_lte = django_filters.NumberFilter(field_name='registrationdate__year', lookup_expr='lte')

    class Meta:
        model = PLD
        fields = [
            'kind',
            'pldtitle',
            'authors',
            'subdivisions',
            'patentowner',
            'panentnumber',
        ]
