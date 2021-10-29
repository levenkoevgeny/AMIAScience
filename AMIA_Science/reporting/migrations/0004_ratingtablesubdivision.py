# Generated by Django 2.2.7 on 2020-01-08 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('reporting', '0003_delete_subdivisiontableemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingTableSubdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Рейтинг в баллах')),
                ('place', models.IntegerField(verbose_name='Итоговое место')),
                ('subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Subdivision', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Рейтинг кафедры',
                'verbose_name_plural': 'Рейтинги кафедр',
                'ordering': ('subdivision',),
            },
        ),
    ]