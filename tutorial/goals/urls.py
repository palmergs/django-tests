from django.conf.urls import url

from . import views

app_name = 'goals'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<goal_id>[0-9]+)$', views.show, name='show'),
	url(r'^(?P<goal_id>[0-9]+)/update$', views.show, name='update'),
	url(r'^(?P<goal_id>[0-9]+)/complete$', views.complete, name='complete'),
]

