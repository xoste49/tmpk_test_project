from django.db import models


class Contract(models.Model):
    """ Договор (номер, ФИО, физ./юр. лицо, статус) """

    number = models.IntegerField(
        verbose_name='Номер договора'
    )

    first_name = models.CharField(
        verbose_name='Имя'
    )

    last_name = models.CharField(
        verbose_name='Фамилия'
    )

    patronymic_name = models.CharField(
        verbose_name='Отчество',
    )

    class ContractType(models.TextChoices):
        NATURAL_PERSON = 'natural_person', 'Физическое лицо'
        LEGAL_PERSON = 'legal_person', 'Юридическое лицо'

    contract_type = models.CharField(
        'физ./юр. лицо',
        choices=ContractType.choices,
        default=ContractType.NATURAL_PERSON,
    )

    status = models.CharField(
        verbose_name='Статус'
    )
