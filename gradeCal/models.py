from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# Reminders:
# Look more into 'User' modules and autheticaton. Turn the Student class into a User class with security and autheticatoin implemented. 

class Student(models.Model):

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name + " " + self.last_name

#Ask abhaya how to get one field to have multiple choicesss
class Course(models.Model):
	student = models.ForeignKey(Student)
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class CourseAssessment(models.Model):
	course = models.ForeignKey(Course)
	title = models.CharField(max_length=50)
	percentage = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class GradeAssessment(models.Model):
	course_assessment = models.ForeignKey(CourseAssessment)
	title = models.CharField(max_length=50)
	score = models.IntegerField(default=0)
	max_score = models.IntegerField(default=0)
	




