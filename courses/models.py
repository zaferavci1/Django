from django.db import models

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    imageUrl = models.CharField()
    date = models.DateTimeField()
    isActive = models.BooleanField()
