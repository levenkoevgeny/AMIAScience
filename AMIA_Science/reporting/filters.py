import django_filters
from sciencework.models import Conference, Statuskonf, Kindkonf, Organizatorforum, Cityforforum
from django import forms


class ConferenceFilter(django_filters.FilterSet):
    conferencename = django_filters.CharFilter(lookup_expr='icontains')
    forumstatus = django_filters.ModelMultipleChoiceFilter(queryset=Statuskonf.objects.all())
    kindforum = django_filters.ModelMultipleChoiceFilter(queryset=Kindkonf.objects.all())
    organizatorforum = django_filters.ModelMultipleChoiceFilter(queryset=Organizatorforum.objects.all())
    forumdate_year = django_filters.NumberFilter(field_name='forumdate__year')
    forumcountry = django_filters.ModelMultipleChoiceFilter(queryset=Cityforforum.objects.all())

    class Meta:
        model = Conference
        fields = ['conferencename', 'forumstatus', 'kindforum', 'organizatorforum', 'forumdate_year', 'forumcountry']



