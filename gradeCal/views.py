from django.shortcuts import render, get_object_or_404

# Create your views here.


from .models import Student, Course

def index(request):
	queryset = Student.objects.all()

	context = {
		'students': queryset,
		'title': 'Grade Wizard Application'
	}
	return render(request, 'gradeCal/index.html', context)

def dashboard(request, id=None):
	student = get_object_or_404(Student, id=id)
	context = {
	"student": student,
	"courses": student.course_set.all(),
	}
	return render(request, 'gradeCal/dashboard.html', context)




















	