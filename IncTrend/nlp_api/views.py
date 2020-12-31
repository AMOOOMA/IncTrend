from django.shortcuts import render

from rest_framework import viewsets

from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('type')
    serializer_class = MessageSerializer
