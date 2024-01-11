from django.db import models

# Create your models here.
class Snake(models.Model):
    name = models.CharField(max_length=100)
    native_to = models.TextField(max_length=300)
    natural_habitat = models.TextField(max_length=300)
    venom_level = models.CharField(max_length=100)
    endangered = models.BooleanField()