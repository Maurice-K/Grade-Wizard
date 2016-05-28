from django.conf.urls import url

from .views import (
	index, 
	dashboard,
	selected_course,
	)


app_name = 'gradeCal'
urlpatterns = [
	# /gradeCal
	url(r'^$', index, name='index'),
	url(r'^(?P<id>\d+)/dashboard/$', dashboard, name='dashboard'),
	url(r'^(?P<id>\d+)/selected_course/$', selected_course, name='selected_course'),
]