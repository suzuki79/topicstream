from django.conf.urls import patterns, url

from topics import views

urlpatterns = patterns('',
    url(r'^$', views.show_all, name='show_all'),
    url(r'^category$', views.get_category_list, name='get_category_list'),
    url(r'^line/(?P<category_cd>[A-Z]+)$', views.get_topic_line, name='get_topic_line'),
    url(r'^detail/(?P<topic_id>.+)/$', views.get_topic_detail, name='get_topic_detail'),
)
