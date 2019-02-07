from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128, help_text='Ex.: Mathematics')

    def __str__(self):
        return self.name


class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    ra = models.CharField(max_length=32, unique=True, verbose_name='Academic Record')

    def __str__(self):
        return self.teacher

