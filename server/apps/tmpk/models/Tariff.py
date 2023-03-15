from django.db import models


class Tariff(models.Model):
    """Тарифы (наименование, стоимость, дата начала действия, дата конца)."""
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

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self) -> str:
        """Model string representation."""
        return f'{self.name}'
