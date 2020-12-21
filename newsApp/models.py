from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50) 
    #Type = models.CharField(max_length=)
    frequency = models.CharField(max_length=10)

def __str__(self):
    return self.name
