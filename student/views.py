# from schoolsystem.student.models import Student
from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm
from.models import Student
from django import forms, test
from django.forms.forms import Form
# # # Create your views here.

def register_student(request):
    form = StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

def register_student(request):
    if request.method=="POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
             form.save()
        else:
            print(form.errors)     
    else:
        form = StudentRegistrationForm()

    return render(request,"register_student.html",{"form":form})  

def Student_list(request):
    student=Student.objects.all()    
    return render(request,"Student_list.html",{"student":student})

def edit_student(request, id):
    student=Student.objects.get(id=id)
    if request.method =="POST":
        Form=StudentRegistrationForm(request.POST, instance =student)
             
    else:
        form =StudentRegistrationForm(instance=student)
        return render (request,"edit_student.html", {"form":form})  

def student_profile(request, id):
    student=Student.objects.get(id=id)
    return render(request, "student_profile.html",{"student":student})

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")




       







