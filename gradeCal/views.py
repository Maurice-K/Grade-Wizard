from django.shortcuts import render, get_object_or_404

# Create your views here.


from .models import Student, AppFunctions
from .forms import TestCreationForm, AssignmentCreationForm, HomeworkCreationForm

def base(request):
	queryset = Student.objects.all()

	context = {
		'students': queryset,
		'title': 'Grade Wizard Application'
	}
	return render(request, 'gradeCal/base.html', context)

def test(request):
	
	context = {"student_first_name": student_first_name}
	return render(request, 'gradeCal/test.html', context)

def test_creation_form(request):
	form = TestCreationForm()
	context = {
		'title': 'Test Creation Form',
		'test_creation_form': form,
	}
	return render(request, 'gradeCal/test_creation_form.html', context)

def assignment_creation_form(request):
	form = AssignmentCreationForm()
	context = {
		'title': 'Assignment Creation Form',
		'assignment_creation_form': form,
	}
	return render(request, 'gradeCal/assignment_creation_form.html', context)

def homework_creation_form(request):
	form = HomeworkCreationForm()
	context = {
		'title': 'Homework Creation Form',
		'homework_creation_form': form,
	}
	return render(request, 'gradeCal/homework_creation_form.html', context)

def completed_test(request):
	form = CompletedHomework()
	context = {
		'title': 'Completed Test',s
		'completed_test': form, 
	}
	return render(request, 'gradeCal/completed_test.html', context)

def completed_assignment(request):
	form = CompletedHomework()
	context = {
		'title': 'Completed Assignment',
		'completed_assignment': form, 
	}
	return render(request, 'gradeCal/completed_assignment.html', context)

def completed_homework(request):
	form = CompletedHomework()
	context = {
		'title': 'Completed Homework',

		'completed_homework': form, 
	}
	return render(request, 'gradeCal/completed_homework.html', context)




	