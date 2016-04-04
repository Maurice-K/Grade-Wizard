from django.conf.urls import url

from . import views


app_name = 'gradeCal'
urlpatterns = [
	# /gradeCal
	url(r'^$', views.base, name='base'),
	url(r'^[0-9]/$', views.test, name='test'),
]