from rest_framework import serializers

from .models import Message, Entry, Company


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'type', 'body']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['fetched_date', 'message', 'prediction', 'parent_company']
