from django.db import models


class VisitCounter(models.Model):
    url_name = models.CharField(max_length=255, blank=True, null=True)
    visit_count = models.IntegerField(verbose_name="Количество посещений", default=0)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Количество посещений'
        verbose_name_plural = 'Количества посещений'