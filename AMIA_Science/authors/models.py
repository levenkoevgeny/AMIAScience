from django.db import models
from django.urls import reverse
from rest_framework import serializers


class Subdivisiongroup(models.Model):
    subdivisiongroupname = models.CharField(max_length=255, verbose_name="Группа подразделений")

    def natural_key(self):
        return (self.subdivisiongroupname)

    def __str__(self):
        return self.subdivisiongroupname

    class Meta:
        ordering = ('subdivisiongroupname',)
        verbose_name = 'Группа подразделений'
        verbose_name_plural = 'Группы подразделений'


class Subdivision(models.Model):
    id_access = models.IntegerField(default=0)
    subdivisionname = models.CharField(max_length=255, verbose_name="Наименование подразделения")
    subdivision_short_name = models.CharField(max_length=70, verbose_name="Сокращенное наименование подразделения",
                                              blank=True, null=True)
    group = models.ForeignKey(Subdivisiongroup, on_delete=models.SET_NULL, null=True)
    img_path = models.TextField(verbose_name="Путь к фото", blank=True, null=True)

    def natural_key(self):
        return (self.subdivisionname)

    def get_by_natural_key(self, subdivisionname):
        return self.get(subdivisionname=subdivisionname)

    def __str__(self):
        return self.subdivisionname

    @property
    def get_capital_name(self):
        return self.subdivisionname.capitalize()

    class Meta:
        ordering = ('subdivisionname',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Position(models.Model):
    id_access = models.IntegerField(default=0)
    positionname = models.CharField(max_length=255, verbose_name="Должность")

    def natural_key(self):
        return (self.positionname)

    def __str__(self):
        return self.positionname

    class Meta:
        ordering = ('positionname',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Candidatespecialty(models.Model):
    candidatespecialtytitle = models.CharField(max_length=255, verbose_name="Название кандидатской диссертации")

    def __str__(self):
        return self.candidatespecialtytitle

    class Meta:
        ordering = ('candidatespecialtytitle',)
        verbose_name = 'Кандидатская специальность'
        verbose_name_plural = 'Кандидатские специальности'


class Doctorspecialty(models.Model):
    doctorspecialtytitle = models.CharField(max_length=255, verbose_name="Название докторской диссертации")

    def __str__(self):
        return self.doctorspecialtytitle

    class Meta:
        ordering = ('doctorspecialtytitle',)
        verbose_name = 'Докторская специальность'
        verbose_name_plural = 'Докторские специальности'

class Rank(models.Model):
    id_access = models.IntegerField(default=0)
    rank = models.CharField(max_length=100, verbose_name="Звание")

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ('id',)
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class Workstatus(models.Model):
    id_access = models.IntegerField(default=0)
    status = models.CharField(max_length=100, verbose_name="Рабочий статус")

    def __str__(self):
        return self.status

    class Meta:
        ordering = ('id',)
        verbose_name = 'Рабочий статус'
        verbose_name_plural = 'Рабочие статусы'


class Author(models.Model):
    id_access = models.IntegerField(default=0)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, null=True, verbose_name="Подразделение")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    firstname = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    dateofbirth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, verbose_name="Звание")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, verbose_name="Должность")
    positiondate = models.DateField(blank=True, null=True, verbose_name="Дата назначения на должность")
    isdocentvak = models.BooleanField(default=False, verbose_name="Является доцентом ВАК")
    docentvakdate = models.DateField(blank=True, null=True, verbose_name="Дата присовения доцента ВАК")
    isprofessor = models.BooleanField(default=False, verbose_name="Является профессором")
    professordate = models.DateField(blank=True, null=True, verbose_name="Дата присвоения профессороской степени")
    iscandidate = models.BooleanField(default=False, verbose_name="Является кандидатом наук")
    candidatedate = models.DateField(blank=True, null=True, verbose_name="Дата присвоения кандидата наук")
    candidatetitle = models.TextField(blank=True, null=True, verbose_name="Название кандидатской диссертации")
    candidatespecialty = models.ForeignKey(Candidatespecialty, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Кандидатская специальность")
    isdoctor = models.BooleanField(default=False, verbose_name="Является доктором наук")
    doctordate = models.DateField(blank=True, null=True, verbose_name="Дата присвоения доктора наук")
    doctortitle = models.TextField(blank=True, null=True, verbose_name="Название докторской диссертации")
    doctorspecialty = models.ForeignKey(Doctorspecialty, on_delete=models.SET_NULL, blank=True, null=True,
                                        verbose_name="Докторская специальность")
    extradata = models.TextField(blank=True, null=True, verbose_name="Дополнительные данные")
    workstatus = models.ForeignKey(Workstatus, on_delete=models.SET_NULL, null=True, verbose_name="Рабочий статус")

    def __str__(self):
        return self.lastname + ' ' + self.firstname + ' ' + self.patronymic + ' ' + str(self.subdivision)

    @property
    def get_short_name(self):
        return self.lastname + ' ' + self.firstname[0] + '.' + self.patronymic[0] + '.'

    def get_absolute_url(self):
        return reverse('authors:list')

    def get_search_filds(self):
        return ['lastname', 'firstname', 'subdivision__subdivisionname']

    class Meta:
        ordering = ('lastname',)
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        exclude = ()
        #fields = ['firstname', 'lastname', 'patronymic']
        depth = 4

class Academicrank(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ученое звание")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Ученое звание'
        verbose_name_plural = 'Ученые звания'


class Academicdegree(models.Model):
    title = models.CharField(max_length=255, verbose_name="Ученая степень")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученые степени'


class OtherAuthor(models.Model):
    lastname = models.CharField(max_length=100, verbose_name="Фамилия", null=True, blank=True)
    initials = models.CharField(max_length=10, verbose_name="Инициалы", null=True, blank=True)
    academicdegree = models.ForeignKey(Academicdegree, on_delete=models.SET_NULL, blank=True, null=True,
                                           verbose_name="Ученая степень")
    academicrank = models.ForeignKey(Academicrank, on_delete=models.SET_NULL, blank=True, null=True,
                                           verbose_name="Ученое звание")
    job = models.CharField(max_length=255, verbose_name="Место работы", null=True, blank=True)
    position = models.CharField(max_length=255, verbose_name="Должность", null=True, blank=True)

    def __str__(self):
        return self.lastname

    class Meta:
        ordering = ('lastname',)
        verbose_name = 'Сторонний автор'
        verbose_name_plural = 'Сторонние авторы'


