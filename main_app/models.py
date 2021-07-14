from django.db import models

# Create your models here.

class Sequence(models.Model):
    sequence = models.TextField(max_length=1000)