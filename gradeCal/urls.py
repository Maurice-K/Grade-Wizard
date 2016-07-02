from django.conf.urls import url

from .views import (
	student_list, 
	dashboard,
	selected_course,
	delete_student,
	modify_student,
	)


app_name = 'gradeCal'
urlpatterns = [
	# /gradeCal
	url(r'^$', student_list, name='student_list'),
	url(r'^(?P<id>\d+)/dashboard/$', dashboard, name='dashboard'),
	url(r'^(?P<id>\d+)/selected_course/$', selected_course, name='selected_course'),
	url(r'^(?P<id>\d+)/delete/$', delete_student, name='delete_student'),
	url(r'^(?P<id>\d+)/modify/$', modify_student, name='modify_student'),
]