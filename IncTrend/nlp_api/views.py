from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('type')
    serializer_class = MessageSerializer


@api_view(['GET', 'POST'])
def handle_company_query(request):
    # TO DO
    return JsonResponse({'hello': 'world'})
