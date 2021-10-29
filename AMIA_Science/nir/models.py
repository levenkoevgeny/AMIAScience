from django.db import models
from authors.models import Author, OtherAuthor, Subdivision


class ReasonNIR(models.Model):
    reasonname = models.CharField(max_length=255)

    def __str__(self):
        return self.reasonname

    class Meta:
        ordering = ('reasonname',)
        verbose_name = 'Основание для проведения НИР'
        verbose_name_plural = 'Основания для проведения НИР'


class Researchresults(models.Model):
    researchresultname = models.CharField(max_length=255)

    def __str__(self):
        return self.researchresultname

    class Meta:
        ordering = ('researchresultname',)
        verbose_name = 'Результат исследования'
        verbose_name_plural = 'Результаты исследования'


class Organization(models.Model):
    organization_name = models.CharField(max_length=255, verbose_name="Название организации")

    def __str__(self):
        return self.organization_name

    class Meta:
        ordering = ('organization_name',)
        verbose_name = 'Организация (сторонние авторы)'
        verbose_name_plural = 'Организации (сторонние авторы)'


class NIR(models.Model):
    nirtitle = models.TextField()
    # reason = models.ForeignKey(ReasonNIR, on_delete=models.SET_NULL, blank=True, null=True)
    reason = models.ManyToManyField(ReasonNIR, through='ReasonInNIR')
    planitem = models.CharField(max_length=255, blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    result = models.ForeignKey(Researchresults, on_delete=models.SET_NULL, blank=True, null=True)
    approvedate = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author)
    authorsother = models.ManyToManyField(OtherAuthor)
    subdivisions = models.ManyToManyField(Subdivision)
    leadersemployees = models.ForeignKey(Author, related_name="nir_leader", on_delete=models.SET_NULL, null=True,
                                         blank=True, verbose_name="Научный руководитель")
    leadersemployeessubdivision = models.ForeignKey(Subdivision, related_name='nir_leadersubdivision',
                                                    on_delete=models.SET_NULL, null=True, blank=True,
                                                    verbose_name="Подразделение научного руководителя")
    leadersnotemployees = models.ForeignKey(OtherAuthor, related_name="nir_leadernotemployee", on_delete=models.SET_NULL,
                                            null=True, blank=True, verbose_name="Научный руководитель (не сотрудник)")
    # anr = models.ForeignKey(ANR, on_delete=models.SET_NULL, blank=True, null=True)
    organization = models.ManyToManyField(Organization, verbose_name="Организация(сторонние авторы)")

    class Meta:
        ordering = ('nirtitle',)
        verbose_name = 'Научно-исследовательская работа'
        verbose_name_plural = 'Научно-исследовательские работы'

    def __str__(self):
        return self.nirtitle

    def get_search_filds(self):
        return ['nirtitle', 'reason__reasonname']

    # def delete(self, *args, **kwargs):
    #     if self.anr:
    #         self.anr.delete()
    #     super(NIR, self).delete(*args, **kwargs)


class ReasonInNIR(models.Model):
    nir = models.ForeignKey(NIR, on_delete=models.CASCADE)
    reason = models.ForeignKey(ReasonNIR, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Основание проведения в НИР(ManyToMany)'
        verbose_name_plural = 'Основания проведения в НИР(ManyToMany)'