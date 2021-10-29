import django_filters
from .models import Dissertationresearch
from authors.models import Author, Subdivision
from django import forms


class Dissertationresearch_Filter(django_filters.FilterSet):

    HALFYEAR_CHOICES = (
        (1, 'Первое'),
        (2, 'Второе'),
    )

    PARTICIPATION_CHOICES = (
        (1, 'Да'),
        (0, 'Нет'),
    )

    author = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all())
    dissertationtheme = django_filters.CharFilter(lookup_expr='icontains')
    result = django_filters.CharFilter(lookup_expr='icontains')
    datebegin = django_filters.NumberFilter(lookup_expr='gte')
    dateend = django_filters.NumberFilter(lookup_expr='lte')
    # is_student_participation = django_filters.ChoiceFilter(choices=PARTICIPATION_CHOICES, widget=forms.Select)
    # halfyear = django_filters.ChoiceFilter(choices=HALFYEAR_CHOICES, widget=forms.Select)
    # year_gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    # year_lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte')

    class Meta:
        model = Dissertationresearch
        fields = ['kind',
                  'status',
                  'dissertationtheme',
                  'reason',
                  'result',
                  'author',
                  'leadersemployees',
                  'leadersemployeessubdivision',
                  'researchplace',
                  'researchplacesubdivision',
                  'datebegin',
                  'dateend'
                  ]

        # kind = models.ForeignKey(Researchkind, on_delete=models.SET_NULL, verbose_name="Вид исследования", null=True,
        #                          blank=True)
        # status = models.ForeignKey(Researchstatus, on_delete=models.SET_NULL, verbose_name="Статус исследователя",
        #                            null=True, blank=True)
        # datebegin = models.IntegerField(verbose_name="Год начала", null=True, blank=True)
        # dateend = models.IntegerField(verbose_name="Год окончания", null=True, blank=True)
        # dissertationtheme = models.TextField(verbose_name="Тема исследования")
        # reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True, blank=True,
        #                            verbose_name="Основание для проведения исследования")
        # result = models.CharField(max_length=255, null=True, blank=True, verbose_name="Результат исследования")
        # otherauthor = models.ForeignKey(OtherAuthor, on_delete=models.SET_NULL, null=True, blank=True,
        #                                 verbose_name="Автор исследования (не сотрудник)")
        # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="author",
        #                            verbose_name="Автор исследования (сотрудник)")
        # leadersemployees = models.ForeignKey(Author, related_name="leadersemployee", on_delete=models.SET_NULL,
        #                                      null=True, blank=True, verbose_name="Научный руководитель (сотрудник)")
        # leadersnotemployees = models.ForeignKey(OtherAuthor, related_name="leadersnotemployee",
        #                                         on_delete=models.SET_NULL, null=True, blank=True,
        #                                         verbose_name="Научный руководитель (не сотрудник)")
        #
        # leadersemployeessubdivision = models.ForeignKey(Subdivision, related_name='leadersemployeessubdivision',
        #                                                 on_delete=models.SET_NULL, null=True, blank=True,
        #                                                 verbose_name="Подразделение научного руководителя")
        # researchplace = models.ForeignKey(Researchplace, on_delete=models.SET_NULL, null=True, blank=True,
        #                                   verbose_name="Место проведения исследования")
        # researchplacesubdivision = models.ForeignKey(Subdivision, related_name='subdivisionplace',
        #                                              on_delete=models.SET_NULL,
        #                                              verbose_name="Подразделение Академии МВД РБ (место проведения)",
        #                                              null=True, blank=True)
