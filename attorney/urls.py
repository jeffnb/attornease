from django.conf.urls import url, patterns
from attorney.views import AttorneyDetailView

urlpatterns = patterns('attorney.views',
    url(r'^(?P<pk>\d+)/$', AttorneyDetailView.as_view(), name='attorney_detail'),
    )