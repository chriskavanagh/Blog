from django.conf.urls import include, url
from . import views

app_name='blog'
urlpatterns = [

    # post list url
    url(r'^$', views.post_list, name='post_list'),
    # post share url
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    # post detail url
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
                                                            views.post_detail,
                                                            name='post_detail'),
]
