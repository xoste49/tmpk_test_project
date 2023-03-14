from django.db import models

from server.apps.main.models import Contract


class CashInflow(models.Model):
    amount = models.DecimalField(
        verbose_name='Сумма'
    )

    date_inflow = models.DateField(
        verbose_name='Дата'
    )

    contract = models.ForeignKey(
        to=Contract,
        verbose_name='Договор',
        related_name='contract_cash_inflow',
        on_delete=models.CASCADE,
    )
