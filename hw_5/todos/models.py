from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'ID {self.id}, name: {self.title}'
