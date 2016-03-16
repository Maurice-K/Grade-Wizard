from django.conf.urls import url

from . import views


app_name = 'gradeCal'
urlpatterns = [
	# /gradeCal
	url(r'^$', views.base, name='base'),
	url(r'^[0-9]/$', views.test, name='test'),
	url(r'^tcf/$', views.test_creation_form, name="test_creation_form"),
	url(r'^hcf/$', views.homework_creation_form, name="homework_creation_form"),
	url(r'^acf/$', views.assignment_creation_form, name="assignment_creation_form"),
]