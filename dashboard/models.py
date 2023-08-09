from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    detail_text = models.TextField()
