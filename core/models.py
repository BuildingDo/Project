from django.db import models

class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.ManyToManyField(Symptom)

    def __str__(self):
        return self.name
