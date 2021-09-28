from django.conf.urls import url
from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet

router=routers.DefaultRouter()
router.register("Students/",StudentViewSet)

urlpatterns = [
    path(" ", include(router.urls)),
]
