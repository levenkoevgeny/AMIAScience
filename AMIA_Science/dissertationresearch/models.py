from django.db import models
from authors.models import Author, Subdivision, OtherAuthor
# from anr.models import ANR


class Researchkind(models.Model):
    kindename = models.CharField(max_length=255)

    def __str__(self):
        return self.kindename

    class Meta:
        ordering = ('kindename',)
        verbose_name = 'Вид исследования'
        verbose_name_plural = 'Виды исследований'


class Researchstatus(models.Model):
    statusname = models.CharField(max_length=255)

    def __str__(self):
        return self.statusname

    class Meta:
        ordering = ('statusname',)
        verbose_name = 'Статус исследователя'
        verbose_name_plural = 'Статусы исследователей'


class Researchplace(models.Model):
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.place

    class Meta:
        ordering = ('place',)
        verbose_name = 'Место проведения исследования'
        verbose_name_plural = 'Места проведения исследований'


class Reason(models.Model):
    reason = models.CharField(max_length=255, verbose_name="Основание")

    def __str__(self):
        return self.reason

    class Meta:
        ordering = ('reason',)
        verbose_name = 'Основание для проведения исследования'
        verbose_name_plural = 'Основания для проведения исследования'


class Dissertationresearch(models.Model):
    kind = models.ForeignKey(Researchkind, on_delete=models.SET_NULL, verbose_name="Вид исследования", null=True, blank=True)
    status = models.ForeignKey(Researchstatus, on_delete=models.SET_NULL, verbose_name="Статус исследователя", null=True, blank=True)
    datebegin = models.IntegerField(verbose_name="Год начала", null=True, blank=True)
    dateend = models.IntegerField(verbose_name="Год окончания", null=True, blank=True)
    dateprotect = models.DateField(verbose_name="Дата защиты", null=True, blank=True)
    dissertationtheme = models.TextField(verbose_name="Тема исследования")
    reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Основание для проведения исследования")
    result = models.CharField(max_length=255, null=True, blank=True, verbose_name="Результат исследования")
    otherauthor = models.ForeignKey(OtherAuthor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Автор исследования (не сотрудник)")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="author", verbose_name="Автор исследования (сотрудник)")
    leadersemployees = models.ForeignKey(Author, related_name="leadersemployee", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Научный руководитель (сотрудник)")
    leadersnotemployees = models.ForeignKey(OtherAuthor, related_name="leadersnotemployee", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Научный руководитель (не сотрудник)")

    leadersemployeessubdivision = models.ForeignKey(Subdivision, related_name='leadersemployeessubdivision', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Подразделение научного руководителя")
    researchplace = models.ForeignKey(Researchplace, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Место проведения исследования")
    researchplacesubdivision = models.ForeignKey(Subdivision, related_name='subdivisionplace', on_delete=models.SET_NULL, verbose_name="Подразделение Академии МВД РБ (место проведения)", null=True, blank=True)
    # anr = models.ForeignKey(ANR, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Диссертационное исследование'
        verbose_name_plural = 'Диссертационные исследования'

    def __str__(self):
        return self.dissertationtheme

    # def delete(self, *args, **kwargs):
    #     if self.anr:
    #         self.anr.delete()
    #     super(Dissertationresearch, self).delete(*args, **kwargs)



