from django import urls
from django.conf.urls import url
from django.db.models.query_utils import select_related_descend
from django.http import response
from .models import Student
from django.test import TestCase
import datetime
from django.urls import reverse
# module that has another module inside 

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="Jane", last_name="AkraChix", age=20)

    def test_first_name_name_contains_first_name(self):
        # assertion to find if something is true or not 
        self.assertIn(self.student.first_name,self.student.full_name())
    
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())
        # how to run it: python manage.py test

    def test_year_of_birth(self):
        year=datetime.datetime.now().year -self.student.age
        self.assertEqual(year, self.student.year_of_birth())

    def test_student_registration_view(self):
        self.data={"first_name":self.student.first_name,"last_name":self.student.last_name, "age":self.student.age}
        urls=reverse("register_student")
        response=self.client.post(urls,self.data)
        self.assertEqual(response.status_code,200)
    

    # def test_student_list
    # test_student_profile
    # test_student_sourse_views

    # HOW TO COLABORATE WITH OTHER PEOPLE WITHOUT INTERFERING WITH OTHER PEOPLES THINGS 