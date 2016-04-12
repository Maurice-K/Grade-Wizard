from django.contrib import admin

# Register your models here.

from .models import Student, Course, CourseAssessment, GradeAssessment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseAssessment)
admin.site.register(GradeAssessment)