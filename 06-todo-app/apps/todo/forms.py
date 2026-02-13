from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_checked']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border rounded px-3 py-2',
                'placeholder': 'Título del TODO'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border rounded px-3 py-2',
                'placeholder': 'Descripción',
                'rows': 4
            }),
            'is_checked': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4'
            })
        }