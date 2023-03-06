from django.db import models


class CashInflow(models.Model):
    amount = models.DecimalField(
        verbose_name='Сумма'
    )

    date_inflow = models.DateField(
        verbose_name='Дата'
    )
