from django.db import models
from django.utils.text import slugify

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateTimeField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)

class category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)