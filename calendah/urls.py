from django.urls import path
from . import views
urlpatterns= [
     path("register/", views.CalendarView.as_view(), name="calendar"),
     path('list/', views.event, name='event_list'),
     ]

