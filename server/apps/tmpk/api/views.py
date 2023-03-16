from datetime import datetime

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from server.apps.tmpk.api.serializers import CashInflowAndSumSerializer, GetContractSerializer
from server.apps.tmpk.models import CashInflow, Contract


class ContractViewSet(RetrieveModelMixin, GenericViewSet):
    """View для работы с договорами."""
    queryset = Contract.objects.prefetch_related('tariffs', 'address').all()
    serializer_class = GetContractSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def get_balance(self, request, pk):
        date = request.query_params.get('date')
        if date is None:
            date = datetime.now().date()
        else:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        qs = CashInflow.objects.prefetch_related('contract').filter(
            contract__id=pk, date_inflow__lte=date,
        )
        data = CashInflowAndSumSerializer(qs).data
        return Response(data)
