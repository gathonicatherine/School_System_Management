from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=10)
    last_name=models.CharField(max_length=25)
    email=models.EmailField(default=30)
    phone_number=models.CharField(max_length=10)
    course=models.CharField(max_length=20)
    trainers_id=models.CharField(max_length=10)
    no_of_lessons_attended=models.PositiveSmallIntegerField(default=1)
    bank_account=models.CharField(max_length=15)
    gender=models.CharField(max_length=15)
    profile_trainer=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    contact=models.CharField(max_length=15)
    image=models.ImageField(default="img.jpeg")
    cv=models.FileField(default="file.pdf")

