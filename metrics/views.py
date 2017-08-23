from datetime import datetime, timedelta

# Create your views here.
from pydruid.utils.filters import Dimension
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


from pydruid.utils.aggregators import hyperunique, doublesum
from pydruid.client import *


def create_druid_client():
    query = PyDruid("http://localhost:8082", 'druid/v2/')
    return query


class CampaignMetrics(GenericAPIView):

    def get(self, request, cid):
        campaign_id = cid
        query =create_druid_client()
        start_date='2017-06-27'
        query_result = query.groupby(
             datasource='celtra3',
             granularity='all',
             dimensions=['adId'],
             intervals=["{0}/p1d".format(start_date)],
             aggregations={'swipes': doublesum('swipes'),
                           'interactions': doublesum('interactions'),
                           'impressions': doublesum('impressions')},
             filter=(Dimension('campaignId') == campaign_id)
        )
        return Response(query_result.result)

class CampiagnMetricsByWeek(GenericAPIView):

    def get(self, request):
        query =create_druid_client()
        last_week_start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        today_date = datetime.now().strftime("%Y-%m-%d")

        query_result = query.groupby(
             datasource='celtra3',
             granularity='week',
             dimensions=['adId'],
             intervals=["{0}/{1}".format(last_week_start_date, today_date)],
             aggregations={'user': hyperunique('user'),'impressions': doublesum('impressions')},
        )

        return Response(query_result.result)
