from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from teacher.api_rest_teacher.viewsets import TeacherViewSet
from student.api_rest_student.viewsets import StudentViewSet
from student.models import Student

router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet, base_name=Student)



urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
