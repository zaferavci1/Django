from django.db import models

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateTimeField()
    isActive = models.BooleanField()

class category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)