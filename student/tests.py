from django.test import TestCase
from .models import *
from teacher.models import Teacher


class StudentTestModel(TestCase):
    """ Test module for student model """


    def setUp(self):
        self.teacher = Teacher.objects.create(name='Gilson')

        self.student = Student.objects.create(
            teacher=self.teacher, name='Lucas',

        )

    def test_models_student(self):
        self.assertEqual(self.student.teacher, self.teacher)
        self.assertEqual(self.student.name, 'Lucas')
