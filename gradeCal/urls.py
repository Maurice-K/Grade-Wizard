from django.conf.urls import url

from . import views


app_name = 'gradeCal'
urlpatterns = [
	# /gradeCal
	url(r'^$', views.index, name='index'),
	url(r'^(?P<id>\d+)/$', views.dashboard, name='dashboard'),
]