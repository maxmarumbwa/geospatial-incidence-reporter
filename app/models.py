from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Incident(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
