from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    major = models.CharField(max_length=255, null=False, blank=False)
    year_of_study = models.IntegerField(null=False)
    faculty = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'ID {self.id}, name: {self.name}, surname: {self.surname}.'