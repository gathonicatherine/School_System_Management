from django.db import models

class Course(models.Model):
   name_of_the_course=models.CharField(max_length=10)
   course_code=models.CharField(max_length=20)
   syllabus=models.CharField(max_length=10)
   description=models.CharField(max_length=20)
   course_unit=models.CharField(max_length=15)
   course_duration=models.CharField(max_length=3)
   course_material=models.CharField(max_length=18)

   def __str__(self):
        return self.first_name

# Create your models here.
