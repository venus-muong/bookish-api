from django.db import models
from django.contrib.postgres.fields import ArrayField

class VisionBoard(models.Model):
    title = models.CharField(max_length=100)
    images = ArrayField(
        models.CharField(max_length=100)
    )
    def __str__(self):
        return self.title