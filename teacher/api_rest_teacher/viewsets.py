from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serielizer import *
from teacher.models import *


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer




