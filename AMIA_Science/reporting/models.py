from django.db import models
from authors.models import Author, Subdivision


class RatingEmployee(models.Model):
    criterion = models.CharField(max_length=255, verbose_name='Критерий')
    value = models.IntegerField(verbose_name='Значение')

    def __str__(self):
        return self.criterion

    class Meta:
        ordering = ('criterion',)
        verbose_name = 'Критерий рейтинга'
        verbose_name_plural = 'Критерии рейтинга'


class RatingTableEmployee(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Сотрудник")
    rating = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Рейтинг в баллах")
    place = models.IntegerField(verbose_name="Итоговое место")

    def __str__(self):
        return 'ППС - ' + self.author.lastname + ' - '  + str(self.rating) + ' баллов'

    class Meta:
        ordering = ('author',)
        verbose_name = 'Рейтинг сотрудника'
        verbose_name_plural = 'Рейтинги сотрудников'


class RatingTableSubdivision(models.Model):
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, verbose_name="Кафедра")
    rating = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Рейтинг в баллах")
    place = models.IntegerField(verbose_name="Итоговое место")

    def __str__(self):
        return 'Кафедра - ' + self.subdivision.subdivision_short_name + ' - '  + str(self.rating) + ' баллов'

    class Meta:
        ordering = ('subdivision',)
        verbose_name = 'Рейтинг кафедры'
        verbose_name_plural = 'Рейтинги кафедр'