import pytest
import json

from django.test import TestCase, Client
from rest_framework import status

client = Client()


def test_api():
    assert True


@pytest.mark.django_db
def test_post_then_get_messages():
    test_message = {'type': 'Test', 'body': 'this is a test message'}
    client.post('/Messages/', test_message, format='json')
    resp = client.get('/Messages/', format='json')
    assert resp.status_code == status.HTTP_200_OK
    assert json.loads(resp.content)[0] == test_message
