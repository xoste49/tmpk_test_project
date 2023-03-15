from django.db import models


class Address(models.Model):
    """Адрес (город, улица, дом, квартира)."""
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

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self) -> str:
        """Model string representation."""
        return f'г. {self.city}, ул. {self.street}, {self.house}, кв. {self.apartment}'
