import json

from app_service.service_helper.base_deal_with import BaseDealWith
from app_service.models import KanmusuEquipment


class EquipmentList(BaseDealWith):
    @staticmethod
    def deal_with(params):
        receive_params = json.loads(params)
        return_list = []
        db_list = KanmusuEquipment.objects.order_by('equipment_id')
        if 'PAGE_SIZE' in receive_params.keys() and 'PAGE_NUM' in receive_params.keys():
            page_size = receive_params['PAGE_SIZE']
            page_num = receive_params['PAGE_NUM']
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
        return json.dumps(return_list)
