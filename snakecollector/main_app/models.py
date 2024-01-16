from django.db import models
from django.urls import reverse

# Create your models here.
class Snake(models.Model):
    name = models.CharField(max_length=100)
    native_to = models.TextField(max_length=300)
    natural_habitat = models.TextField(max_length=300)
    diet = models.TextField(max_length=125, default='Food')
    venom_level = models.CharField(max_length=100)
    endangered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'snake_id': self.id})