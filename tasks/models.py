from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')  # Add a default empty string
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
