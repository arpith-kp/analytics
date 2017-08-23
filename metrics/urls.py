from django.conf.urls import include, url

import views

urlpatterns = [
    url(r'^api/v1/metrics/campaign/(?P<campaign_id>[A-Za-z]+)$', views.CampaignMetrics.as_view()),
    url(r'^last_week$', views.CampiagnMetricsByWeek.as_view()),
]