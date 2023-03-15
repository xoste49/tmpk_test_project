from server.apps.tmpk.models import Contract


def get_contract_info(number: int) -> Contract:
    """Получение данных по договору."""
    try:
        contract = Contract.objects.get(number=number)
        return contract
    except Contract.DoesNotExist:
        raise Exception('Договор не найден.')

