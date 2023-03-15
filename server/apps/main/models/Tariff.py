from django.db import models


class Tariff(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=255,
    )
    price = models.IntegerField(
        verbose_name='Стоимость',
        max_length=255,
    )

    date_start = models.DateField(
        verbose_name='Дата начала действия',
        max_length = 255,
    )

    date_end = models.DateField(
        verbose_name='Дата конца действия',
        max_length=255,
    )
