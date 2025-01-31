from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    text = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f'ID {self.id}, title: {self.title}.'