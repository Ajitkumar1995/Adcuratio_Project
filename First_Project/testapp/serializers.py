from rest_framework import serializers
from testapp.models import Invoice
class InvoiceSerializer(serializers.Serializer):
    seller = serializers.CharField(max_length=64)
    buyer = serializers.CharField(max_length=64)
    invoice_no = serializers.CharField(max_length=64)
    date = serializers.CharField(max_length=64)
    def create(self,validated_data):
        return Invoice.objects.create(**validated_data)
    #partial updation
    def update(self,instance,validated_data):
        instance.seller=validated_data.get('seller',instance.seller)
        instance.buyer=validated_data.get('buyer',instance.buyer)
        instance.invoice_no=validated_data.get('invoice_no',instance.invoice_no)
        instance.date=validated_data.get('date',instance.date)
        instance.save()
        return instance