from django.db import models
from authors.models import Author, Subdivision, OtherAuthor


class PLDkind(models.Model):
    kindtitle = models.CharField(max_length=255, verbose_name="Вид")

    def __str__(self):
        return self.kindtitle

    class Meta:
        ordering = ('kindtitle',)
        verbose_name = 'Вид патентно-лицензионной деятельности'
        verbose_name_plural = 'Виды патентно-лицензионной деятельности'


class PatentOwner(models.Model):
    ownername = models.CharField(max_length=255, verbose_name="Патентообладатель")

    def __str__(self):
        return self.ownername

    class Meta:
        ordering = ('ownername',)
        verbose_name = 'Патентообладатель'
        verbose_name_plural = 'Патентообладатели'


class PLD(models.Model):
    kind = models.ForeignKey(PLDkind, on_delete=models.SET_NULL, verbose_name="Вид ПЛД", blank=True, null=True)
    pldtitle = models.CharField(max_length=255, verbose_name="Название ПЛД")
    actionstart = models.DateField(blank=True, null=True, verbose_name="Начало действия")
    registrationdate = models.DateField(blank=True, null=True, verbose_name="Дата регистрации")
    requestdate = models.DateField(blank=True, null=True, verbose_name="Дата подачи заявки")
    authors = models.ManyToManyField(Author, verbose_name="Автор")
    authorsother = models.ManyToManyField(OtherAuthor, verbose_name="Сторонний автор")
    subdivisions = models.ManyToManyField(Subdivision, verbose_name="Подразделение")
    patentowner = models.ManyToManyField(PatentOwner, through='PatentownerInPLD', verbose_name="Патентообладатель")
    panentnumber = models.CharField(max_length=255, verbose_name="Номер панетна", blank=True, null=True)

    def __str__(self):
        return self.pldtitle

    def get_search_filds(self):
        return ['pldtitle']

    class Meta:
        ordering = ('pldtitle',)
        verbose_name = 'Патентно-лицензионная деятельность'
        verbose_name_plural = 'Патентно-лицензионные деятельности'


class PatentownerInPLD(models.Model):
    pld = models.ForeignKey(PLD, on_delete=models.CASCADE)
    patentowner = models.ForeignKey(PatentOwner, on_delete=models.CASCADE)

    def __str__(self):
        return self.pld.pldtitle + " " + self.patentowner.ownername

    class Meta:
        verbose_name = 'Патентообладатели в ПЛД'
        verbose_name_plural = 'Патентообладатели в ПЛД'