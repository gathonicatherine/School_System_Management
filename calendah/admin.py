from django.contrib import admin
from django.conf.urls import url
from django.urls.conf import path
from django.urls.resolvers import URLPattern

from.models import Event
admin.site.register(Event)

# Register your models here.
