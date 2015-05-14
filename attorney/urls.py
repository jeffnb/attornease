from django.conf.urls import url, patterns
from attorney.views import AttorneyDetailView, AttorneyListView

urlpatterns = patterns('attorney.views',
    url(r'^(?P<pk>\d+)/$', AttorneyDetailView.as_view(), name='attorney_detail'),
    url(r'^area/(?P<area_id>\d+)/category/(?P<cat_id>\d+)/$', AttorneyListView.as_view(), name='attorney_list_cat'),
    url(r'^area/(?P<area_id>\d+)$', AttorneyListView.as_view(), name='attorney_list'),
    )