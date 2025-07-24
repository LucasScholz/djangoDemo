from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed']
        labels = {
            "title" : "Beschreibung",
            "completed" : "Beendet?",
        }
