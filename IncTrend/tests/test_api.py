import pytest
import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


def test_api():
    assert True


@pytest.mark.django_db
def test_post_then_get_messages():
    client = Client()
    test_message = {'id': 1, 'type': 'Test', 'body': 'this is a test message'}
    client.post('/Messages', test_message, format='json')
    resp = client.get('/Messages', format='json')
    assert resp.status_code == status.HTTP_200_OK
    assert json.loads(resp.content)[0] == test_message


@pytest.mark.django_db
def test_get_predictions_create_company():
    client = Client()
    test_names = ['AAPL', 'AMZN', 'AAPL', 'AMZN', 'GOOGL']
    for name in test_names:
        resp = client.get(reverse('company-predictions', args=(name,)))
        assert resp.status_code == status.HTTP_200_OK

    resp = client.get('/Company', format='json')
    assert resp.status_code == status.HTTP_200_OK
    assert len(json.loads(resp.content)) == 3   # make sure no duplicates added
