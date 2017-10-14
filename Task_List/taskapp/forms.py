from django.forms import ModelForm
from taskapp.models import Tasks

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['text']
