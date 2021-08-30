from django import forms
from django.forms import fields
from django.db import models
from .models import Course 


class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ="__all__"