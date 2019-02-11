from rest_framework.viewsets import ModelViewSet
from .serielizer import *
from student.models import *


class StudentViewSet(ModelViewSet):
    # """ para projetos mais simples esta forma é mais simples"""
    #
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer
    serializer_class = StudentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return  Student.objects.all()

    def list(self, request, *args, **kwargs):
        return super(StudentViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(StudentViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(StudentViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(StudentViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(StudentViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(StudentViewSet, self).partial_update(request, *args, **kwargs)

