from datetime import datetime, timedelta

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from server.apps.tmpk.api.serializers import GetContractSerializer, CashInflowAndSumSerializer
from server.apps.tmpk.models import Contract, CashInflow


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

        data = CashInflowAndSumSerializer(CashInflow.objects.prefetch_related('contract').filter(contract__id=pk)).data
        return Response(data)

        # try:
        #
        #     message_text = SMSTemplate.objects.get(pk=pk).text
        #     if 'leads[add][0][id]' in data:
        #         lead_id = data['leads[add][0][id]'][0]
        #     elif 'leads[status][0][id]' in data:
        #         lead_id = data['leads[status][0][id]'][0]
        #     else:
        #         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #     lead_info = get_lead_info(lead_id).json()
        #     contact_id = lead_info['_embedded']['contacts'][0]['id']
        #     contact_info = get_contact_info(contact_id).json()
        #     contact_phone = None
        #     for field in contact_info['custom_fields_values']:
        #         if field['field_name'] == 'Телефон':
        #             contact_phone = '+' + field['values'][0]['value']
        #     if not contact_phone:
        #         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #     # Проверка разрешено ли клиенту отправлять SMS уведомления
        #     if User.objects.filter(phone=contact_phone, allow_sms=True).exists():
        #         SmsSender(phone=contact_phone, text=message_text, plain_text=True)()
        #
        # except Exception:  # noqa: PIE786
        #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # return Response(status=status.HTTP_200_OK)
