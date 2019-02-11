from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from student.models import Student
from teacher.models import Teacher
from teacher.api_rest_teacher.serielizer import TeacherSerializer


class StudentSerializer(ModelSerializer):

    teacher = TeacherSerializer()
    resource_uri = SerializerMethodField

    class Meta:
        model = Student
        fields = ['name', 'id', 'resource_uri', 'teacher']

    def create(self, validated_data):
        related_data = validated_data.pop('teacher')
        teacher = Teacher.objects.get(**related_data)
        student = Student.objects.create(teacher=teacher, **validated_data)
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
