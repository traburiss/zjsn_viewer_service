from app_service.service_helper.error_deal import ErrorDeal
from app_service.service_helper.code_deal.equipment_list import EquipmentList

code_map = {
    'error': ErrorDeal.deal_with,
    '1': EquipmentList.deal_with,
}
