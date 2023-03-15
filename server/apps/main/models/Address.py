from django.db import models


class Address(models.Model):
    city = models.CharField(
        verbose_name='Город',
        max_length=255,
    )

    street = models.CharField(
        verbose_name='Улица',
        max_length=255,
    )

    house = models.CharField(
        verbose_name='Дом',
        max_length=255,
    )

    apartment = models.CharField(
        verbose_name='Квартира',
        max_length=255,
    )



