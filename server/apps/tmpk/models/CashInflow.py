from django.db import models


class CashInflow(models.Model):
    """Приходы денежных средств на договор (сумма, дата)."""
    amount = models.DecimalField(
        verbose_name='Сумма',
        decimal_places=2,
        max_digits=20,
    )

    date_inflow = models.DateField(
        verbose_name='Дата'
    )

    contract = models.ForeignKey(
        to='tmpk.Contract',
        verbose_name='Договор',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Приход денежных средств'
        verbose_name_plural = 'Приходы денежных средств'

    def __str__(self) -> str:
        """Model string representation."""
        return f'{self.amount} {self.date_inflow} {self.contract}'
