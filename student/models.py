from django.db import models
from teacher.models import Teacher


class Student(models.Model):
    """
    Student Model
    Defines the attributes of a student
    Model one-to-many
    """
    teacher = models.ForeignKey(Teacher, related_name='teacher', on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    
    def resource_uri(self):
        return '/api/v1/{}/{}/'.format(
            self.__class__._meta.app_label, self.pk
        )

