from django.contrib import admin
from testapp.models import Invoice
# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display=['id','seller','buyer','invoice_no','date']
admin.site.register(Invoice,InvoiceAdmin)
