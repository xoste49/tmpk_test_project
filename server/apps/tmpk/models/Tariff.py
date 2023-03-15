from django.db import models


class Tariff(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    price = models.IntegerField(
        verbose_name='Стоимость',
    )

    date_start = models.DateField(
        verbose_name='Дата начала действия',
    )

    date_end = models.DateField(
        verbose_name='Дата конца действия',
    )
