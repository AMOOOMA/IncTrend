from rest_framework import serializers

from .models import Message
from .models import Entry


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'type', 'body']


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['fetched_date', 'message', 'prediction']
