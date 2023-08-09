from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    text = models.TextField(blank=True, max_length=2000)
    datetime = models.DateField(default=datetime.now(), blank=True)

