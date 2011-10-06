from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.core.serializers import serialize
from django.db.models import Q

from models import Address

def get_address(request):
    results = []
    json = {'success':'False'}
    if request.method == "GET":
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']           
            model_results = Address.objects.filter(
                Q(code__icontains=value)
                | Q(city__icontains=value)
                | Q(town__icontains=value)
                | Q(area__icontains=value)
                | Q(block__icontains=value)
            )
            json = serialize("json", model_results, ensure_ascii=False)
            
        if request.GET.has_key(u'callback'):
            json = "%s(%s)" % (request.GET[u'callback'],json)
    
    return HttpResponse(json, mimetype='application/json')