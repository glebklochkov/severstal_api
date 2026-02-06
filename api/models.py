from django.db import models

# Create your models here.
class Task(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active'
        COMPLETED = 'completed'

    title = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices = Status.choices,
        default = Status.ACTIVE,
    )
    description = models.TextField(blank=True)