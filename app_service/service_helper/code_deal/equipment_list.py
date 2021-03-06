import json

from app_service.service_helper.base_deal_with import BaseDealWith
from app_service.models import KanmusuEquipment
from json import JSONDecodeError


class EquipmentList(BaseDealWith):
    @staticmethod
    def deal_with(params):
        try:
            receive_params = json.loads(params)
        except JSONDecodeError as e:
            return json.dumps({"error_code": "1", "error_type": "params error"})
        return_list = []
        db_list = KanmusuEquipment.objects.order_by('equipment_id')
        if isinstance(receive_params, dict) and 'PAGE_SIZE' in receive_params.keys() and 'PAGE_NUM' in receive_params.keys():
            page_size = int(receive_params['PAGE_SIZE'])
            page_num = int(receive_params['PAGE_NUM'])
            start_count = page_size * (page_num - 1)
            end_count = page_size * page_num
            db_list_len = len(db_list)
            if db_list_len < start_count + 1:
                db_list = []
            elif db_list_len < end_count:
                end_count = db_list_len
            db_list = db_list[start_count:end_count]

        for row in db_list:
            if row is not None:
                return_list.append(row.to_dict())

        result = {'error_info': 'success', 'result': return_list}
        return json.dumps(result)
