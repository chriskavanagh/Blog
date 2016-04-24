from django.conf.urls import include, url
from . import views
from .feeds import LatestPostsFeed


app_name='blog'
urlpatterns = [

    # post list url
    url(r'^$', views.post_list, name='post_list'),
    # post list by tag
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    # post share url
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    # Search url
    url(r'^search/$', views.post_search, name='post_search'),
    # post detail url
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
                                                            views.post_detail,
                                                            name='post_detail'),
    # feed urls
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
]
