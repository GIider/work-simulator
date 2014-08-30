from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^(\w*)', views.page, name='page'),
)