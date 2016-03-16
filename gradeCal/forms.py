from django import forms


from .models import Student, Course, Test, Homework, Assignment

class TestCreationForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ["title", ]

class AssignmentCreationForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = ["title"]

class HomeworkCreationForm(forms.ModelForm):
	class Meta:
		model = Homework
		fields = ["title"]

class CompletedHomework(forms.ModelForm):
	class Meta:
		model = Homework
		fields = ['score', 'max_score']

class CompletedAssignment(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = ['score', 'max_score']

class CompletedTest(forms.ModelForm):
	class Meta:
		model = Test
		fields = ['score', 'max_score']