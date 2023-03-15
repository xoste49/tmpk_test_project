# Generated by Django 3.2.18 on 2023-03-15 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('house', models.CharField(max_length=255, verbose_name='Дом')),
                ('apartment', models.CharField(max_length=255, verbose_name='Квартира')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('date_start', models.DateField(verbose_name='Дата начала действия')),
                ('date_end', models.DateField(verbose_name='Дата конца действия')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер договора')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('contract_type', models.CharField(choices=[('natural_person', 'Физическое лицо'), ('legal_person', 'Юридическое лицо')], default='natural_person', max_length=255, verbose_name='физ./юр. лицо')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
                ('address', models.ManyToManyField(to='tmpk.Address', verbose_name='Адреса')),
                ('tariffs', models.ManyToManyField(to='tmpk.Tariff', verbose_name='Тарифы')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Договора',
            },
        ),
        migrations.CreateModel(
            name='CashInflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма')),
                ('date_inflow', models.DateField(verbose_name='Дата')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmpk.contract', verbose_name='Договор')),
            ],
            options={
                'verbose_name': 'Приход денежных средств',
                'verbose_name_plural': 'Приходы денежных средств',
            },
        ),
    ]
