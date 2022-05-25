import json
from django.views.generic import TemplateView
from .forms import ServiceImportForm
from django.shortcuts import redirect, render
from models.nomenclature.models import Nomenclature
import pandas
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.paginator import Paginator
from .serializers import NomenclatureFilterSerializer
from models.nomenclature.category_choices import CATEGORY_CHOICES, MARK_CHOICES


class ServiceImportView(TemplateView):
    template_name = 'service/import_export.html'
    form_class = ServiceImportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nomenclatures'] = Nomenclature.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            data = pandas.read_excel(form.cleaned_data['excel_file'])
            json_data = json.loads(data.to_json(orient='records'))
            nomenclature = Nomenclature.objects.get(id=form.cleaned_data['nomenclature_id'])
            nomenclature.services = json_data

            return redirect('home', orgID=self.kwargs['orgID'])
        else:
            context = self.get_context_data()
            context['form'] = form

            return render(self.request, template_name=self.template_name, context=context)


class ServiceListView(TemplateView):
    template_name = 'service/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        context['marks'] = MARK_CHOICES
        context['nomenclatures'] = Nomenclature.objects.all()
        return context


class NomenclatureItemsFilterApiView(GenericAPIView):
    serializer_class = NomenclatureFilterSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.GET)

        if serializer.is_valid():
            filtered_data = self.get_filtered_services(
                serializer.data.get('search'),
                serializer.data.get('category'),
                serializer.data.get('mark')
            )

            paginated_data = self.get_paginated_data_page_number(
                filtered_data,
                page=serializer.data.get('page'),
                limit=serializer.data.get('limit')
            )

            return Response(paginated_data)
        else:
            return Response(serializer.errors)

    def get_filtered_services(self, search='', category='', mark=''):
        services = Nomenclature.objects.get(id=self.kwargs['id']).services
        filtered_services = []

        for service in services:
            if (
                    (
                            search.lower() in service['Название'].lower()
                            or search.lower() in service['Категория'].lower()
                            or search.lower() in service['Марка'].lower()
                    )
                    and category in service['Категория']
                    and mark in service['Марка']
            ):
                filtered_services.append(service)

        return filtered_services

    def get_paginated_data_page_number(self, data, page=1, limit=None):
        paginator = Paginator(data, limit)
        page_number = paginator.num_pages
        paginated_data = paginator.page(page).object_list

        return {
            "services": paginated_data,
            "page_number": page_number
        }


class ServiceExportView(TemplateView):
    """Экспортировать услуги"""
    template_name = 'service/import.html'
