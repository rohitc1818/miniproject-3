from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    ranl = models.IntegerField()
    age = models.IntegerField()
    marks = models.IntegerField()

