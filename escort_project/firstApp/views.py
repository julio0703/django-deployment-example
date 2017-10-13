from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Escort
from .forms import EscortForm
from django.views.generic import (ListView, CreateView,
                                  DetailView, UpdateView,
                                  DeleteView, )

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact_page(request):
    return render(request,'contact.html')

class EscortListView(ListView):
    model = Escort
    context_object_name = 'escorts'

class CreateEscortView(CreateView):
    model = Escort
    form_class = EscortForm

class DetailEscortView(DetailView):
    model = Escort

class UpdateExcortView(UpdateView):
    model = Escort
    form_class = EscortForm

class DeleteEscortView(DeleteView):
    model = Escort
    success_url = reverse_lazy('escort_list')
