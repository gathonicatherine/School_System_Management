from django.conf.urls import url
from django.contrib import admin
from django.urls.conf import path
from django.urls.resolvers import URLPattern

from.models import Student
admin.site.register(Student)
