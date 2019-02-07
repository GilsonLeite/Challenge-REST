from django.test import TestCase
from .models import *


class TeacherTestModel(TestCase):

    def setUp(self):
        self.teacher = Teacher.objects.create(
            name='Gilson', email='test@gmail.com', subject='POO'
        )

        self.student = Student.objects.create(
            teacher=self.teacher, name='Lucas',
            email='lucas@teste.com', ra='1234'
        )

    def test_models_teacher(self):
        self.assertEqual(self.teacher.name, 'Gilson')
        self.assertEqual(self.teacher.email, 'test@gmail.com')
        self.assertEqual(self.teacher.subject, 'POO')

    def test_models_student(self):
        self.assertEqual(self.student.name, 'Lucas')
        self.assertEqual(self.student.email, 'lucas@teste.com')
        self.assertEqual(self.student.ra, '1234')

    def test_models_foreingkey(self):
        self.assertEqual(self.student.teacher, self.teacher)




