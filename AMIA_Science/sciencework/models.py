from django.db import models
from authors.models import Author, Subdivision
from django.urls import reverse
from rest_framework import serializers


class Publicationkind(models.Model):
    id_access = models.IntegerField(default=0)
    publicationkind = models.CharField(max_length=255)

    def __str__(self):
        return self.publicationkind

    class Meta:
        ordering = ('publicationkind',)
        verbose_name = 'Вид публикации'
        verbose_name_plural = 'Виды публикации'


class Grif(models.Model):
    grifname = models.CharField(max_length=255)

    def __str__(self):
        return self.grifname

    class Meta:
        ordering = ('grifname',)
        verbose_name = 'Гриф'
        verbose_name_plural = 'Грифы'


class Interest(models.Model):
    interestname = models.CharField(max_length=255)

    def __str__(self):
        return self.interestname

    class Meta:
        ordering = ('interestname',)
        verbose_name = 'В чьих интересах'
        verbose_name_plural = 'В чьих интересах'


class InternationalBase(models.Model):
    basename = models.CharField(max_length=255)

    def __str__(self):
        return self.basename

    class Meta:
        ordering = ('basename',)
        verbose_name = 'Международная база научного тестирования'
        verbose_name_plural = 'Международные базы научного тестирования'


class Magazine(models.Model):
    magazinename = models.CharField(max_length=255)
    invak = models.BooleanField(blank=True, null=True)
    ininternational = models.ManyToManyField(InternationalBase, verbose_name="Международная база научного цитирования", blank=True)

    def __str__(self):
        return self.magazinename

    class Meta:
        ordering = ('magazinename',)
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'


class Digest(models.Model):
    digestname = models.CharField(max_length=255)
    invak = models.BooleanField(blank=True, null=True)
    ininternational = models.ManyToManyField(InternationalBase, verbose_name="Международная база научного цитирования", blank=True)

    def __str__(self):
        return self.digestname

    class Meta:
        ordering = ('digestname',)
        verbose_name = 'Сборник статей'
        verbose_name_plural = 'Сборники статей'


class Statuskonf(models.Model):
    statusname = models.CharField(max_length=255)

    def __str__(self):
        return self.statusname

    class Meta:
        ordering = ('statusname',)
        verbose_name = 'Статус начного форума'
        verbose_name_plural = 'Статусы научных форумов'


class Kindkonf(models.Model):
    kindname = models.CharField(max_length=255)

    def __str__(self):
        return self.kindname

    class Meta:
        ordering = ('kindname',)
        verbose_name = 'Вид научного форума'
        verbose_name_plural = 'Виды научных форумов'


class Organizatorforum(models.Model):
    orgname = models.CharField(max_length=255)

    def __str__(self):
        return self.orgname

    class Meta:
        ordering = ('orgname',)
        verbose_name = 'Организатор форума'
        verbose_name_plural = 'Организаторы форумов'


class Cityforforum(models.Model):
    cityforumtitle = models.CharField(max_length=100)

    def __str__(self):
        return self.cityforumtitle

    class Meta:
        ordering = ('cityforumtitle',)
        verbose_name = 'Страна проведения форума'
        verbose_name_plural = 'Страны проведения форума'


class Conference(models.Model):
    conferencename = models.TextField(verbose_name="Название конференции")
    conferencename_short = models.TextField(verbose_name="Название конференции(сокращенное)", blank=True, null=True)
    forumstatus = models.ForeignKey(Statuskonf, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Статус научного форума")
    kindforum = models.ForeignKey(Kindkonf, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Вид научного форума")
    organizatorforum = models.ForeignKey(Organizatorforum, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Организатор научного форума")
    forumdate = models.DateField(blank=True, null=True, verbose_name="Дата проведения")
    forumcountry = models.ForeignKey(Cityforforum, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Страна проведения")
    moderators = models.ManyToManyField(Author, verbose_name="Модераторы научного форума/руководители секции", blank=True)

    def __str__(self):
        return str(self.conferencename_short)

    class Meta:
        ordering = ('conferencename',)
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'


class Publisher(models.Model):
    publishername = models.CharField(max_length=255)

    def __str__(self):
        return self.publishername

    class Meta:
        ordering = ('publishername',)
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Subspecies(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Подвид учебного издания'
        verbose_name_plural = 'Подвиды учебных изданий'


class Orgfounder(models.Model):
    orgname = models.CharField(max_length=255)

    def __str__(self):
        return self.orgname

    class Meta:
        ordering = ('orgname',)
        verbose_name = 'Организация учредитель сборника'
        verbose_name_plural = 'Организации учредители сборников'


class Publication(models.Model):
    id_access = models.IntegerField(default=0)
    kind = models.ForeignKey(Publicationkind, on_delete=models.SET_NULL, null=True)

    year = models.IntegerField(blank=True, null=True)
    halfyear = models.CharField(max_length=100, default="Не указано")
    outputdata = models.TextField(blank=True, null=True)
    sheetcount = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True)
    grif = models.ForeignKey(Grif, on_delete=models.SET_NULL, blank=True, null=True)
    magazine = models.ForeignKey(Magazine, on_delete=models.SET_NULL, blank=True, null=True)
    digest = models.ForeignKey(Digest, on_delete=models.SET_NULL, blank=True, null=True)
    invak = models.BooleanField(blank=True, null=True)
    ininternationals = models.ManyToManyField(InternationalBase)
    interest = models.ForeignKey(Interest, on_delete=models.SET_NULL, blank=True, null=True)
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL, blank=True, null=True)
    is_forum_result = models.BooleanField(verbose_name="По итогам научного форума", default=False)
    workisforeignauthors = models.BooleanField(blank=True, null=True)
    authorcount = models.IntegerField(default=0, blank=True, null=True)
    scienceworkstudentparticipation = models.BooleanField(blank=True, null=True, default=False)
    authors = models.ManyToManyField(Author, through='AuthorsInPublication')
    subdivisions = models.ManyToManyField(Subdivision)

    forumcountry = models.ForeignKey(Cityforforum, on_delete=models.SET_NULL, blank=True, null=True)
    subspecies = models.ForeignKey(Subspecies, on_delete=models.SET_NULL, blank=True, null=True)
    orgfounders = models.ForeignKey(Orgfounder, on_delete=models.SET_NULL, blank=True, null=True)
    forumstatus = models.ForeignKey(Statuskonf, on_delete=models.SET_NULL, blank=True, null=True)
    kindforum = models.ForeignKey(Kindkonf, on_delete=models.SET_NULL, blank=True, null=True)
    organizatorforum = models.ForeignKey(Organizatorforum, on_delete=models.SET_NULL, blank=True, null=True)
    forumdate = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ('kind',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        if self.outputdata is None:
            return "blank" 
        return self.outputdata

    def get_search_filds(self):
        return ['outputdata']

    def get_absolute_url(self):
        return reverse('sciencework:updatesciencework')

    # def delete(self, *args, **kwargs):
    #     if self.anr:
    #         self.anr.delete()
    #     super(Publication, self).delete(*args, **kwargs)


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        exclude = ()
        depth = 4


class AuthorsInPublication(models.Model):
    id_access = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True)
    isauthor = models.BooleanField(default=False)

    def __str__(self):
        if (self.author is not None and self.publication is not None):
            return self.author.lastname + " " + self.publication.outputdata + " авторство - " + str(self.isauthor)
        else:
            return "Id_access {}".format(self.id_access)

    class Meta:
        verbose_name = 'Авторы публикации'
        verbose_name_plural = 'Авторы публикаций'
