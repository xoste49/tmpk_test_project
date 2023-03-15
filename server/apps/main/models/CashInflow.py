from django.db import models


class CashInflow(models.Model):
    amount = models.DecimalField(
        verbose_name='Сумма',
        decimal_places=2,
        max_digits=20,
    )

    date_inflow = models.DateField(
        verbose_name='Дата'
    )

    contract = models.ForeignKey(
        to='models.Contract',
        verbose_name='Договор',
        on_delete=models.CASCADE,
    )
