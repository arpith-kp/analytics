from django.test import TestCase

# Create your tests here.
from mock import patch, Mock

from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from voluptuous import Schema
import django

class CampaignMetricsTest(TestCase):

    def setUp(self):
        super(TestCase, self).setUp()
        django.setup()

    @patch('metrics.views.PyDruid.groupby')
    def test_campaign_metrics_get(self, mock_client):
        mock_response = [
            {
            "event": {
            "adId": "1030",
            "impressions": 108.0,
            "interactions": 104.0,
            "swipes": 101.0
        },
        "timestamp": "2017-06-27T00:00:00.000Z",
        "version": "v1"
        }]
        mock_client.return_value = Mock(name='first',result=Mock(name='second', data=mock_response, content=mock_response, return_value=mock_response))
        client = APIClient()
        response = client.get(reverse('get_metrics_by_id', args=[100]))
        assert response.status_code == 200
        Schema(response.json()) ==  Schema(mock_response)
