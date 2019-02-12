from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from teacher.api_rest_teacher.viewsets import TeacherViewSet
from student.api_rest_student.viewsets import StudentViewSet

router = routers.DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
