from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from teacher.models import Teacher


class TeacherSerializer(ModelSerializer):

    resource_uri = SerializerMethodField

    class Meta:
        model = Teacher
        fields = ['name', 'resource_uri', 'id']

