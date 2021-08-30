# from schoolsystem.student.models import Student
from django.shortcuts import render
from .forms import StudentRegistrationForm
from.models import Student
from django import forms
# # # Create your views here.

def register_student(request):
    form = StudentRegistrationForm()
    return render(request,"register_student.htm",{"form":form})

def register_student(request):
    if request.method=="POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
             form.save()
        else:
            print("form".errors)     
    else:
        form = StudentRegistrationForm()

    return render(request,"register_student.htm",{"form":form})  

def Student_list(request):
    student=Student.objects.all()    
    return render(request,"Student_list.htm",{"student":student})








