from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from attorney.views import IndexPageView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^attorneys/', include('attorney.urls')),
    url(r'^errors/404', TemplateView.as_view(template_name="404.html"), name="404_error"),
    url(r'^$', IndexPageView.as_view(), name="index"),
)
