from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'goals'
urlpatterns = [
    url(r'^$', views.index, name='goal_index'),
	url(r'^new/$', views.create, name='goal_new'),
	url(r'^(?P<goal_id>[0-9]+)/$', views.show, name='goal_show'),
	url(r'^(?P<goal_id>[0-9]+)/edit$', views.update, name='goal_edit'),
	url(r'^(?P<goal_id>[0-9]+)/delete$', views.destroy, name='goal_delete'),
	url(r'^(?P<goal_id>[0-9]+)/complete$', views.complete, name='goal_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
