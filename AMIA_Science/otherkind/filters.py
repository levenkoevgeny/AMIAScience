import django_filters
from .models import Otherkind, Council, Work, Institution, ActivityKind, Dissertation_kind, Edition_name
from authors.models import Author, Subdivision
from sciencework.models import Organizatorforum


class OtherKindFilter(django_filters.FilterSet):
    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    subdivisions = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())
    year_gte = django_filters.NumberFilter(field_name='other_year', lookup_expr='gte')
    year_lte = django_filters.NumberFilter(field_name='other_year', lookup_expr='lte')
    research_theme = django_filters.CharFilter(field_name='research_theme', lookup_expr='icontains')
    study_name = django_filters.CharFilter(field_name='study_name', lookup_expr='icontains')
    group_establishment = django_filters.CharFilter(field_name='group_establishment', lookup_expr='icontains')
    participation_result = django_filters.CharFilter(field_name='participation_result', lookup_expr='icontains')
    research_institution = django_filters.CharFilter(field_name='research_institution', lookup_expr='icontains')
    work_reason = django_filters.CharFilter(field_name='work_reason', lookup_expr='icontains')
    work_kind = django_filters.CharFilter(field_name='work_kind', lookup_expr='icontains')

    class Meta:
        model = Otherkind
        fields = [
            'activity',
            'сouncil',
            'completed_work_council',
            'institution',
            'dissertation_kind',
            'edition_name',
            'founder',
            'completed_work_editoral'
        ]
