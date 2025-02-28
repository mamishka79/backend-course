from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return f'ID {self.id}, name: {self.title}, description: {self.description}'
