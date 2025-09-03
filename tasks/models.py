from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
def default_due_date():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    class Meta:
        ordering = ['-created_at']


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank= True, null= True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=default_due_date)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name= "items", null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['due_date']
