from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Task)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'due_date', 'completed', 'todo_list')
