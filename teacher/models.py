from django.db import models


class Teacher(models.Model):
    """
    Teacher Model
    Defines the attributes of a teacher
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    @property
    def resource_uri(self):
        return '/api/v1/{}/{}/'.format(
            self.__class__._meta.app_label, self.pk
        )


