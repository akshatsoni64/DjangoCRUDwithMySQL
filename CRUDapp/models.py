from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    eno = models.CharField(max_length=10)
