from django.db import models
from django.urls import reverse

# Create your models here.
class Tasks(models.Model):
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('about')
