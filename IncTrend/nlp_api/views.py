from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import MessageSerializer, CompanySerializer, EntrySerializer
from .models import Message, Company, Entry
from .predict import Predict
from datetime import datetime


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
    entries = list(Entry.objects.filter(parent_company=company))
    if len(entries) <= 0 or (entries[0].fetched_date - datetime.now()).days > 0:  # don't use if fetched older than one day
        print('no cached entries or entries expired')
        for entry in entries:  # delete the expired entries if any
            entry.delete()

        predictions = Predict(name).get_predictions()
        if predictions is not None:
            for prediction, message in predictions:
                entry = Entry.create(message, prediction, company)
                entry.save()
                entries.append(entry)

    print(entries)
    entries_serializer = EntrySerializer(entries, many=True)

    return JsonResponse(entries_serializer.data, safe=False)
