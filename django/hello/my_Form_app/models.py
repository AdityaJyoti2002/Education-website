from django.db import models

# Create your models here.
class Log(models.Model):
    name = models.CharField(max_length=112)
    email = models.CharField(max_length=112)
    phone = models.CharField(max_length=112)
    #password = models.CharField(max_length=112)
    feedback = models.TextField()
    date = models.DateField()

def __str__(self):
    return self.name

