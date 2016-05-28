from django.shortcuts import render, get_object_or_404

# Create your views here.


from .models import Student, Course
from .forms import CourseCreationForm, StudentCreationForm

def index(request):
	students = Student.objects.all()
	#Creating a New Student - Begin - 
	form = StudentCreationForm(request.POST or None)
	if form.is_valid():
		form.save(commit=False)
	#Creating a New Student - End -
	context = {
		'form': form, 
		'students': students,
		'title': 'Grade Wizard Application'
	}
	return render(request, 'gradeCal/index.html', context)

def dashboard(request, id=None):
	student = get_object_or_404(Student, id=id)
	form = CourseCreationForm(request.POST or None, initial={'student': student})
	if form.is_valid():
		form.save(commit=False)
	context = {
		"form": form,
		"student": student,
		"courses": student.course_set.all(),
	}
	return render(request, 'gradeCal/dashboard.html', context)

def selected_course(request, id=None):
	course = get_object_or_404(Course, id=id)
	enrolled_student = course.student
	context = {
	"enrolled_student": enrolled_student,
	"course": course,
	"course_assessments": course.courseassessment_set.all(),
	}
	return render(request, 'gradeCal/selected_course.html', context)






















	