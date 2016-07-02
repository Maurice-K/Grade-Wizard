from django.shortcuts import render
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)
from .forms import UserLoginForm
# Create your views here.



def login_view(request):
	form = UserLoginForm(request.POST or None):
		if form.is_valid:
			username = form.get_cleaned_data('username')
			password = form.get_cleaned_data('password')
	context = {
		'username': username
		'password': password
	}
	return render(request, "", context)



def register_view(request):
	context = {}
	return render(request, "", context)



def logout_view(request):
	context = {}
	return render(request, "", context)