from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from .serializers import StudentSerializers



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
