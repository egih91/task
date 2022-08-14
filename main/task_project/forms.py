from .models import Task
from  django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class TaskForm(ModelForm):
        class Meta:
            model = Task
            fields = ['title', "task"]
            widgets = {
                "title": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': "Введите название"
                }),
            "task": Textarea(attrs={'class': 'form-control', 'placeholder': "Введите задачу"}),
            #"date": DateTimeInput(attrs={'class': 'form-control','placeholder': "Дата публикации"}),
            }