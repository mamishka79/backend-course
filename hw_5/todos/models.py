from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, null=False, on_delete=models.CASCADE, default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID {self.id}, name: {self.title}'
