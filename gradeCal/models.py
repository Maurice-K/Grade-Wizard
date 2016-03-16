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

	# Contstants per object created
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)

	# Overall Percentage of anything distributed across the course
	test_percentage = models.IntegerField(default=0)
	homework_percentage = models.IntegerField(default=0)
	assignment_percentage = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Test(models.Model):

	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	score = models.FloatField(default=0.0)
	max_score = models.FloatField(default=0.0)

	def finalPercentage(self):
		return self.score / self.max_score

	#Grab Value from the parent of the current object to return the overall value it is to the grade of the course
	def courseValue(self):
		return self.finalPercentage * self.course.test_percentage 

	def __str__(self):
		return self.title

class Homework(models.Model):

	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	score = models.FloatField(default=0.0)
	max_score = models.FloatField(default=0.0)

	def finalPercentage(self):
		return self.score / self.max_score

	def __str__(self):
		return self.title

class Assignment(models.Model):

	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	score = models.FloatField(default=0.0)
	max_score = models.FloatField(default=0.0)

	def finalPercentage(self):
		return self.score / self.max_score

	def __str__(self):
		return self.title



class AppFunctions():	
	def navbar_navigate_to(self, url_name):
		return reverse(url_name, kwargs={})
