from rest_framework import serializers
from student.models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=("first_name", "last_name","age")