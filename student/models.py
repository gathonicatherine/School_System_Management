from django.db import models
from PIL import Image 


class Student(models.Model):
    first_name=models.CharField(max_length=10, default="Nowamani")
    last_name = models.CharField(max_length=10, default="Rue",)
    age = models.PositiveSmallIntegerField(default=29)
    date_of_birth = models.DateField()
    national_id = models.CharField(max_length=9, default=867)
    email = models.EmailField(default="anyijanet@gmail.com")
    registration = models.PositiveIntegerField(default=1324)
    phone_number = models.PositiveIntegerField(default=283957)
    guardian_name = models.CharField(max_length=15,default="Muhammed",null=True,blank=True)
    guardian_contacts = models.PositiveIntegerField(default=3245)
    country = models.CharField(max_length=20, default=40,null=True,blank=True)
    medical_report = models.FileField(default="default.png",null=True,blank=True)
    class_name = models.CharField(max_length=12, default=30,null=True,blank=True)
    room_number = models.CharField(max_length=15, default=60,null=True,blank=True)
    big_sister = models.CharField(max_length=20, default=40)
    mentors_name = models.CharField(max_length=35, default=50,null=True,blank=True)
    passport_photo = models.ImageField(default="default.jpeg",null=True,blank=True)
    profile=models.ImageField(default="default.jpng")

    def __str__(self):
        return self.first_name

        
