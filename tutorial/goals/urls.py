from django.conf.urls import url
from . import views

app_name = 'goals'
urlpatterns = [
    url(r'^$', views.index, name='goal_index'),
	url(r'^new/$', views.goal_new, name='goal_new'),
	url(r'^(?P<goal_id>[0-9]+)/$', views.show, name='goal_show'),
	url(r'^(?P<goal_id>[0-9]+)/update$', views.show, name='goal_edit'),
	url(r'^(?P<goal_id>[0-9]+)/complete$', views.complete, name='goal_complete'),
]

