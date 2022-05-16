from django.contrib import admin
from .models import Contractor


# Register your models here.
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    """Контрагент"""
    list_display = ('id', 'name', 'address', 'IIN_or_BIN',
                    'bank_requisition', 'phone', 'trust_person', 'organisation')
    list_display_links = ('id', 'name',)
