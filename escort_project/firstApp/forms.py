from django.forms import ModelForm
from .models import Escort

class EscortForm(ModelForm):
    class Meta:
        model = Escort
        fields = ['name','image','story','interest','rate']
