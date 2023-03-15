from django.db import models

from server.apps.main.models import Address, Tariff


class Contract(models.Model):
    """Договор (номер, ФИО, физ./юр. лицо, статус) """

    number = models.IntegerField(
        verbose_name='Номер договора'
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length = 255,
    )

    patronymic_name = models.CharField(
        verbose_name='Отчество',
        max_length=255,
    )

    class ContractType(models.TextChoices):
        NATURAL_PERSON = 'natural_person', 'Физическое лицо'
        LEGAL_PERSON = 'legal_person', 'Юридическое лицо'

    contract_type = models.CharField(
        'физ./юр. лицо',
        choices=ContractType.choices,
        default=ContractType.NATURAL_PERSON,
        max_length=255,
    )

    status = models.CharField(
        verbose_name='Статус',
        max_length = 255,
    )

    address = models.ManyToManyField(
        to=Address,
        verbose_name='Адреса',
    )

    tariffs = models.ManyToManyField(
        to=Tariff,
        verbose_name='Тарифы',
    )
