from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.serializers import InvoiceSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from testapp.models import Invoice
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class InvoiceCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            inv=Invoice.objects.get(id=id)
            serializer=InvoiceSerializer(inv)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Invoice.objects.all()
        serializer=InvoiceSerializer(qs,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=InvoiceSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource created Successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        inv=Invoice.objects.get(id=id)
        serializer=InvoiceSerializer(inv,data=pdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'Resource updated Successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json', status=400)

    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        inv=Invoice.objects.get(id=id)
        inv.delete()
        msg={'msg':'Resource Deleted Successfully'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')
