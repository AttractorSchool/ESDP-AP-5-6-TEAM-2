from models.contractor.models import Contractor
from models.organization.models import Organization
from django.shortcuts import get_object_or_404


def create_contractor(data):
    Contractor.objects.create(
        name=data['name'],
        address=data['address'],
        IIN_or_BIN=data['IIN_or_BIN'],
        bank_requisition=data['bank_requisition'],
        phone=data['phone'],
        trust_person=data['trust_person'],
        organisation=get_object_or_404(Organization, id=1),
    )