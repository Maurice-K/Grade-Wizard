from django import forms


from .models import Course, Student


class CourseCreationForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title', 'student']
		widgets = {'student': forms.HiddenInput()}


class StudentCreationForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['first_name', 'last_name']