#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

from django.http import HttpResponse
from django.http import StreamingHttpResponse

from . import operation_tpl


def hello(request):

    return HttpResponse("Hello world ! ")


def do(request):
    module_name = request.GET["moduleName"]
    project_name = request.GET["projectName"]
    project_id = operation_tpl.gen_tpl(module_name, project_name)
    result = {
        "projectId": project_id.__str__()
    }
    return HttpResponse(json.dumps(result), content_type="application/json")


def download(request):
    project_id = request.GET["projectId"]
    project_info = operation_tpl.get(project_id)
    response = StreamingHttpResponse(project_info["zip_file"], content_type='application/zip')
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(project_info["zip_name"])
    return response
