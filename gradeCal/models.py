from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name + " " + self.last_name

	def get_absolute_url(self):
		return reverse('gradeCal:index')

class Course(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	
	def __str__(self):
		return self.title


#Table that handles each course's grade distribution.
#Ex: Final worth 35 percent, Midterm worth 30 percent, Homework/Assignments worth 15 percent, Quizzes worth 20 percent

class CourseAssessment(models.Model):
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=50)
	percentage = models.IntegerField(default=0)

	def __str__(self):
		return self.title


#Grades that belong in course assessment
#Ex: Homework #1 scored 30/40, Midterm scored 85/100
class GradeAssessment(models.Model):
	course_assessment = models.ForeignKey(CourseAssessment)
	title = models.CharField(max_length=50)
	score = models.IntegerField(default=0)
	max_score = models.IntegerField(default=0)

	def __str__(self):
		return self.title
	




