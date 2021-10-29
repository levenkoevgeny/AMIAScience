from django.db import models
from authors.models import Author, Subdivision, OtherAuthor
from sciencework.models import Publication
from nir.models import NIR
from dissertationresearch.models import Dissertationresearch


class Developmentkind(models.Model):
    kindtitle = models.CharField(max_length=255, verbose_name="Вид внедренной разработки")

    def natural_key(self):
        return self.kindtitle

    def __str__(self):
        return self.kindtitle

    class Meta:
        ordering = ('kindtitle',)
        verbose_name = 'Вид внедренной разработки'
        verbose_name_plural = 'Виды внедренной разработки'


class Introductionkind(models.Model):
    introductionkindtitle = models.CharField(max_length=255, verbose_name="Вид внедрения")

    def natural_key(self):
        return self.introductionkindtitle


    def __str__(self):
        return self.introductionkindtitle

    class Meta:
        ordering = ('introductionkindtitle',)
        verbose_name = 'Вид внедрения'
        verbose_name_plural = 'Виды внедрения'


class Introductionorganization(models.Model):
    organizationname = models.CharField(max_length=255, verbose_name="Организация внедрения")

    def natural_key(self):
        return self.organizationname

    def __str__(self):
        return self.organizationname

    class Meta:
        ordering = ('organizationname',)
        verbose_name = 'Организация внедрения'
        verbose_name_plural = 'Организации внедрения'


class ANR(models.Model):
    developmentkind = models.ForeignKey(Developmentkind, on_delete=models.SET_NULL, verbose_name="Вид внедренной разработки", blank=True, null=True)
    introductionkind = models.ForeignKey(Introductionkind, on_delete=models.SET_NULL, verbose_name="Вид внедрения", blank=True, null=True)
    introductionorganization = models.ForeignKey(Introductionorganization, on_delete=models.CASCADE, verbose_name="Организация внедрения")
    approvedate = models.DateField(verbose_name="Дата внедрения")
    halfyear = models.CharField(max_length=1, blank=True, null=True, verbose_name="Полугодие внедрения")
    authors = models.ManyToManyField(Author, verbose_name="Авторы-сотрудники Академии", blank=True)
    authorsother = models.TextField(verbose_name="Сторонние авторы", blank=True, null=True);
    # authorsother = models.ManyToManyField(OtherAuthor, verbose_name="Сторонние авторы")
    subdivisions = models.ManyToManyField(Subdivision, verbose_name="Подразделения разработки")
    year = models.IntegerField(verbose_name="Год", blank=True, null=True)
    is_student_participation = models.BooleanField(verbose_name="Участие обучающихся", blank=True, null=True)
    # student = models.ForeignKey(OtherAuthor, on_delete=models.CASCADE, verbose_name="Обучающйися", related_name="anr_participation", blank=True, null=True)
    student = models.TextField(verbose_name="Обучающйися", blank=True, null=True);
    development_has_not_base = models.BooleanField(verbose_name="Разработка, отсутствует в базе(boolean)", blank=True, null=True)
    development_without_base = models.TextField(verbose_name="Разработка, отсутствующая в базе", blank=True, null=True)
    sciencework = models.ForeignKey(Publication, on_delete=models.CASCADE, verbose_name="Публикация", blank=True, null=True)
    nir = models.ForeignKey(NIR, on_delete=models.CASCADE, verbose_name="Научно-исследовательская работа", blank=True, null=True)
    dissertation = models.ForeignKey(Dissertationresearch, on_delete=models.CASCADE, verbose_name="Диссертационное исследование", blank=True, null=True)
    adjunct = models.TextField(verbose_name="Адъюнкт", blank=True, null=True);

    def __str__(self):
        return self.developmentkind.kindtitle

    class Meta:
        ordering = ('developmentkind',)
        verbose_name = 'Апробация научных результатов'
        verbose_name_plural = 'Апробации научных результатов'




