from django.db import models


class Address(models.Model):
    city = models.CharField(
        verbose_name='Город',
    )

    street = models.CharField(
        verbose_name='Улица',
    )

    house = models.CharField(
        verbose_name='Дом',
    )

    apartment = models.CharField(
        verbose_name='Квартира',
    )



