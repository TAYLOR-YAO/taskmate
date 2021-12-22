from django import forms
from django.forms import fields
from todolist_app.models import Tasklist


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task', 'done']
