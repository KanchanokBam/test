from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=128, primary_key=True)
    course_name = models.CharField(max_length=128)
    teacher = models.CharField(max_length=128)
