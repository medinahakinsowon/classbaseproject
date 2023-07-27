from django.db import models

# Create your models here.#the model is for the database

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.name)
    