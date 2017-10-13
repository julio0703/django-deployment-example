from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from django.urls import reverse
# Create your models here.
class Escort(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media',blank=True,null=True)
    story = models.TextField()
    interest = models.TextField()
    rate = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('firstApp:escort_list')

    def __str__(self):
        return self.name
