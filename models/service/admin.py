from import_export import resources
from django.contrib import admin
from .models import Service
from import_export.admin import ImportExportModelAdmin


class ServiceResource(resources.ModelResource):
    """Для импорта и экспорта данных услуг"""
    class Meta:
        model = Service


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    """Услуги"""
    resource_class = ServiceResource
    list_display = ('id', 'name', 'category',
                    'price', 'note', 'price_category',)
    list_display_links = ('id', 'name', )