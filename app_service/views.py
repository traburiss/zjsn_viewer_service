from django.http import HttpResponse
from app_service.service_helper.code_map import code_map
# Create your views here.


def app_service(request):

    function_code = request.GET.get('function_code')
    send_params = request.GET.get('send_params')

    if function_code is None:
        function_code = "error"
    if function_code not in code_map.keys():
        function_code = "error"
    return HttpResponse(code_map.get(function_code)(send_params))
