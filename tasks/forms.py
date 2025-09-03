from django import forms
from django.forms import ModelForm
from .models import *


class TaskList(forms.ModelForm):


    class Meta:
        model = ToDoList
        fields = ["title"] 


class TaskForm(forms.ModelForm):


    class Meta:
        model = Task
        fields = "title description due_date completed".split()

        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }