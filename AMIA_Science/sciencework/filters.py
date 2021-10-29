import django_filters
from .models import Publication, Digest, Magazine, InternationalBase, Conference, Statuskonf, Kindkonf, \
    Organizatorforum, Cityforforum, Publicationkind
from authors.models import Author, Subdivision
from django import forms

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


# class CustomFilterList(django_filters.FilterSet):
#     def filter(self, qs, value):
#         if value not in (None, ''):
#             values = [v for v in value.split(',')]
#             return qs.filter(**{'%s__%s' % (self.field_name, self.lookup_expr): values})
#         return qs

class ScienceWork_Filter(django_filters.FilterSet):
    HALFYEAR_CHOICES = (
        (1, 'Первое'),
        (2, 'Второе'),
    )

    PARTICIPATION_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )

    # authors = NumberInFilter(queryset=Author.objects.all(), lookup_expr='in')
    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    kind = django_filters.ModelMultipleChoiceFilter(queryset=Publicationkind.objects.all())
    subdivisions = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    halfyear = django_filters.ChoiceFilter(choices=HALFYEAR_CHOICES, widget=forms.Select)
    workisforeignauthors = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    scienceworkstudentparticipation = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    is_forum_result = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    invak = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    forumdate = django_filters.DateFilter(widget=myDateInput)
    year_gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte')
    ininternationals = django_filters.ModelChoiceFilter(queryset=InternationalBase.objects.all())
    outputdata = django_filters.CharFilter(lookup_expr='icontains')
    forumcountry = django_filters.ModelChoiceFilter(field_name='conference__forumcountry',
                                                    queryset=Cityforforum.objects.all())
    forumstatus = django_filters.ModelChoiceFilter(field_name='conference__forumstatus',
                                                   queryset=Statuskonf.objects.all())
    kindforum = django_filters.ModelChoiceFilter(field_name='conference__kindforum',
                                                 queryset=Kindkonf.objects.all())
    organizatorforum = django_filters.ModelChoiceFilter(field_name='conference__organizatorforum',
                                                        queryset=Organizatorforum.objects.all())

    class Meta:
        model = Publication
        fields = [
            'kind',
            'year',
            'halfyear',
            'outputdata',
            'sheetcount',
            'publisher',
            'grif',
            'magazine',
            'digest',
            'invak',
            'interest',
            'conference',
            'workisforeignauthors',
            'scienceworkstudentparticipation',
            'authors',
            'subdivisions',
            'subspecies',
            'ininternationals'
        ]


class Conference_Filter(django_filters.FilterSet):
    conferencename = django_filters.CharFilter(lookup_expr='icontains')
    forumstatus = django_filters.ModelChoiceFilter(queryset=Statuskonf.objects.all())
    kindforum = django_filters.ModelChoiceFilter(queryset=Kindkonf.objects.all())
    organizatorforum = django_filters.ModelChoiceFilter(queryset=Organizatorforum.objects.all())
    forumdate = django_filters.NumberFilter(field_name='forumdate__year')
    forumcountry = django_filters.ModelChoiceFilter(queryset=Cityforforum.objects.all())
    moderators = django_filters.ModelChoiceFilter(queryset=Author.objects.all())

    class Meta:
        model = Conference
        fields = '__all__'
