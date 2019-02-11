from django.test import TestCase
from .models import *


class TeacherTestModel(TestCase):
    """ Test module for teacher model """

    def setUp(self):
        self.teacher = Teacher.objects.create(name='Gilson')

    def test_models_teacher(self):
        self.assertEqual(self.teacher.name, 'Gilson')





