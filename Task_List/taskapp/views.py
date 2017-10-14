from django.shortcuts import render
from .models import Tasks
from .forms import TasksForm
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, CreateView,
                                  UpdateView, DetailView,
                                  ListView, )
# Create your views here.
class TaskListView(ListView):
    model = Tasks
    template_name = 'tasks_list.html'
    context_object_name = 'task'

class CreateTaskView(CreateView):
    template_name = 'tasks_form.html'
    model = Tasks
    form_class = TasksForm
    success_url = reverse_lazy('task_list')

class UpdateTaskView(UpdateView):
    template_name = 'tasks_form.html'
    model = Tasks
    form_class = TasksForm
    success_url = reverse_lazy('task_list')

class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'tasks_detail.html'
