from django.db.models.aggregates import Sum
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from server.apps.tmpk.models import Contract, Address, Tariff, CashInflow


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class TariffSerializer(ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class GetContractSerializer(ModelSerializer):
    address = AddressSerializer(many=True, read_only=True)
    tariffs = TariffSerializer(many=True, read_only=True)

    class Meta:
        model = Contract
        fields = '__all__'


class CashInflowSerializer(ModelSerializer):
    class Meta:
        model = CashInflow
        fields = '__all__'


class CashInflowAndSumSerializer(Serializer):
    inflows = SerializerMethodField()
    sum = SerializerMethodField()

    def get_inflows(self, cashinflow: CashInflow) -> dict:
        return CashInflowSerializer(cashinflow, many=True).data

    def get_sum(self, cashinflow: CashInflow) -> float or None:
        aggregate = cashinflow.aggregate(Sum('amount'))
        return aggregate['amount__sum']

    class Meta:
        fields = ['inflows', 'sum']
