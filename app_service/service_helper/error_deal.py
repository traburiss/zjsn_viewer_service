import json
from app_service.service_helper.base_deal_with  import BaseDealWith


class ErrorDeal(BaseDealWith):
    @staticmethod
    def deal_with(params):
        # get_params = json.loads(params)
        result = {'error_info': 'no such function', 'result': params}
        return json.dumps(result)
