from django.contrib import admin

from server.apps.tmpk.models import Contract, Address, Tariff, CashInflow


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin[Contract]):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin[Address]):
    pass


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin[Tariff]):
    pass


@admin.register(CashInflow)
class CashInflowAdmin(admin.ModelAdmin[CashInflow]):
    pass
