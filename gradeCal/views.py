from django.shortcuts import render, get_object_or_404

# Create your views here.


from .models import Student

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





















	