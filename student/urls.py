from django.urls import path
from .views import Student_list, delete_student, register_student, student_profile
from .views import edit_student, register_student, Student_list

urlpatterns= [
    path("register/", register_student,name="register_student"),
    path("list/",Student_list, name="Student_list"),
    path("edit/<int:id>/", edit_student, name= "edit_student"),
    path("profile/<int:id>/", student_profile, name = "student_profile"),
    path("delete/<int:id>/", delete_student, name="delete_student")
    ]