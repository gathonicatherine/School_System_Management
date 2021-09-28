from django.shortcuts import render
from .models import Course

from .forms import CourseRegistrationForm
def register_course(request):
    # if request.method =="POST":
    #     form=CourseRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         print(form.errors)
    # else:
    form=CourseRegistrationForm()
    return render(request, "register_course.html", {'form':form})  

def Course_list(request):
    courses=Course.objects.all()    
    return render(request,"Course_list.html",{"course":courses})

# Create your views here.
