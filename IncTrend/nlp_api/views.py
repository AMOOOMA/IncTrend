from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import MessageSerializer, CompanySerializer, EntrySerializer
from .models import Message, Company, Entry
from .predict import Predict


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('type')
    serializer_class = MessageSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('fetched_date')
    serializer_class = EntrySerializer


@api_view(['GET'])
def handle_company_query(request, name):
    company = None
    if len(Company.objects.filter(name=name)) > 0:  # make new company object is not found in db
        company = Company.objects.get(name=name)
    else:
        company = Company.create(name)
        company.save()

    # attempt to find cached Entries
    entries = Entry.objects.filter(parent_company=company)
    if len(entries) > 0:  # check for cached entries
        print(entries)
        # to do: check date
    else:
        predictions = Predict(name).get_predictions()
        print('no entries')
        # to do

    return JsonResponse({'hello': name})
