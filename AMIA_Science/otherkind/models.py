from django.db import models
from authors.models import Author, Subdivision, OtherAuthor
from sciencework.models import Organizatorforum


class CouncilCategory(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="Категория совета")

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Категория совета'
        verbose_name_plural = 'Категории советов'


class Council(models.Model):
    сounciltitle = models.CharField(max_length=255, verbose_name="Название совета")
    category = models.ForeignKey(CouncilCategory, on_delete=models.SET_NULL, verbose_name="Категория", blank=True, null=True)

    def natural_key(self):
        return (self.сounciltitle)

    def __str__(self):
        return self.сounciltitle

    class Meta:
        ordering = ('сounciltitle',)
        verbose_name = 'Вид совета'
        verbose_name_plural = 'Виды совета'


class Work(models.Model):
    worktitle = models.CharField(max_length=255, verbose_name="Название работы")

    def natural_key(self):
        return (self.worktitle)

    def __str__(self):
        return self.worktitle

    class Meta:
        ordering = ('worktitle',)
        verbose_name = 'Работа, выполненная в составе совета'
        verbose_name_plural = 'Работы, выполненные в составе совета'


class Institution(models.Model):
    institutionname = models.CharField(max_length=255, verbose_name="Название учреждения")

    def natural_key(self):
        return (self.institutionname)

    def __str__(self):
        return self.institutionname

    class Meta:
        ordering = ('institutionname',)
        verbose_name = 'Учреждение, при котором действует совет'
        verbose_name_plural = 'Учреждения, при которых действует совет'



class ActivityKind(models.Model):
    activitytitle = models.CharField(max_length=255, verbose_name="Вид деятельности")

    def natural_key(self):
        return (self.activitytitle)

    def __str__(self):
        return self.activitytitle

    class Meta:
        ordering = ('activitytitle',)
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'

class Dissertation_kind(models.Model):
    kind_title = models.CharField(max_length=255, verbose_name="Вид диссертации")

    def __str__(self):
        return self.kind_title

    class Meta:
        ordering = ('kind_title',)
        verbose_name = 'Вид диссертации'
        verbose_name_plural = 'Виды диссертаций'


class Edition_name(models.Model):
    edition_name = models.CharField(max_length=255, verbose_name="Наименование научного издания")

    def __str__(self):
        return self.edition_name

    class Meta:
        ordering = ('edition_name',)
        verbose_name = 'Наименование научного издания'
        verbose_name_plural = 'Наименования научных изданий'


class Otherkind(models.Model):
    activity = models.ForeignKey(ActivityKind, on_delete=models.SET_NULL, verbose_name="Вид деятельности", blank=True, null=True)

    # Советы
    сouncil = models.ForeignKey(Council, on_delete=models.SET_NULL, verbose_name="Совет", blank=True, null=True)
    completed_work_council = models.ForeignKey(Work, on_delete=models.SET_NULL, related_name="council_work", verbose_name="Работа, выполненная в составе совета", blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, verbose_name="Учреждение, при котором действует совет", blank=True, null=True)

    # Оппонирование диссертационных исследований
    dissertation_kind = models.ForeignKey(Dissertation_kind, on_delete=models.SET_NULL, verbose_name='Вид диссертации', blank=True, null=True)
    defense_place = models.CharField(max_length=255, verbose_name="Место защиты", blank=True, null=True)
    research_theme = models.CharField(max_length=255, verbose_name="Тема исследования", blank=True, null=True)
    aspirant = models.ForeignKey(OtherAuthor, on_delete=models.SET_NULL, verbose_name="Соискатель", blank=True, null=True)
    defense_date = models.DateField(verbose_name="Дата защиты", blank=True, null=True)

    # Нормативно-правовые акты
    work_reason = models.CharField(max_length=255, verbose_name="Основание проведения работ", blank=True, null=True)
    work_kind = models.CharField(max_length=255, verbose_name="Вид работы", blank=True, null=True)
    work_subcontractors = models.CharField(max_length=255, verbose_name="Соисполнители", blank=True, null=True)

    # Редакционные коллегии
    edition_name = models.ForeignKey(Edition_name, on_delete=models.SET_NULL, verbose_name="Наименование научного издания", blank=True, null=True)
    founder = models.ForeignKey(Organizatorforum, on_delete = models.SET_NULL, verbose_name="Учредитель научного издания", blank = True, null=True)
    completed_work_editoral = models.ForeignKey(Work, on_delete=models.SET_NULL, related_name="editoral_work", verbose_name="Работа, выполненная в составе редколлегии", blank=True, null=True)

    # Рабочие группы
    study_name = models.TextField(verbose_name="Наименование исследования, основание включения в состав рабочей группы", blank=True, null=True)
    group_establishment = models.CharField(max_length=255, verbose_name="Учреждение, в котором создана рабочая группа(ВНК)", blank=True, null=True)
    participation_result = models.CharField(max_length=255, verbose_name="Результат участия", blank=True, null=True)

    # Подготовка отзывов (экспертных заключений) на диссертационные исследования
    research_institution = models.CharField(max_length=255, verbose_name="Учреждение (организация), представившее исследование", blank=True, null=True)
    research_institution = models.CharField(max_length=255, verbose_name="Учреждение (организация), представившее исследование", blank=True, null=True)

    # Общие поля
    authors = models.ManyToManyField(Author, verbose_name="Члены совета")
    subdivisions = models.ManyToManyField(Subdivision)
    other_year = models.IntegerField(verbose_name="Год", blank=True, null=True)

    def __str__(self):
        return self.activity.activitytitle

    def get_search_filds(self):
        return ['сouncil__сounciltitle', 'dissertation_kind__kind_title', 'work_kind', 'edition_name__edition_name', 'study_name']

    class Meta:
        ordering = ('id',)
        verbose_name = 'Иной вид деятельности'
        verbose_name_plural = 'Иные виды деятельности'