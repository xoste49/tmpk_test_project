from django.contrib import admin
from django.utils.html import format_html

from server.apps.tmpk.models import Contract, Address, Tariff, CashInflow


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin[Contract]):
    list_display = ('number', 'first_name', 'last_name', 'patronymic_name', 'contract_type', 'status', 'get_address', 'get_tariffs')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tariffs', 'address')

    @admin.display(description='Адреса')
    def get_address(self, obj):
        return format_html("<br>".join([str(a) for a in obj.address.all()]))

    @admin.display(description='Тарифы')
    def get_tariffs(self, obj):
        return format_html("<br>".join([str(t) for t in obj.tariffs.all()]))


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin[Address]):
    list_display = ('city', 'street', 'house', 'apartment')


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin[Tariff]):
    list_display = ('name', 'price', 'date_start', 'date_end')


@admin.register(CashInflow)
class CashInflowAdmin(admin.ModelAdmin[CashInflow]):
    list_display = ('amount', 'date_inflow', 'contract')
