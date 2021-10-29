import django_filters
from nir.models import NIR, ReasonNIR
from authors.models import Author, Subdivision
from django import forms


myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})


class NIR_Filter(django_filters.FilterSet):
    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    subdivisions = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    reason = django_filters.ModelMultipleChoiceFilter(queryset=ReasonNIR.objects.all())
    startdate_since = django_filters.NumberFilter(lookup_expr='gte', field_name='startdate__year')
    startdate_till = django_filters.NumberFilter(lookup_expr='lte', field_name='startdate__year')
    enddate_since = django_filters.NumberFilter(lookup_expr='gte', field_name='enddate__year')
    enddate_till = django_filters.NumberFilter(lookup_expr='lte', field_name='enddate__year')
    approvedate = django_filters.DateFilter(widget=myDateInput)
    leadersemployees = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    leadersemployeessubdivision = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    nirtitle = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = NIR
        fields = ['nirtitle', 'reason', 'planitem', 'result', 'approvedate', 'authors', 'subdivisions', 'leadersemployees', 'leadersemployeessubdivision', 'startdate_since',
                  'startdate_till', 'enddate_since', 'enddate_till']

