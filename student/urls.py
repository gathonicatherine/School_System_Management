from django.urls import path
from .views import Student_list, register_student
from .models import Student

urlpatterns= [
    path("register/", register_student,name="register_student"),
    path("list/",Student_list, name="Student_list")
    ]