from django.db import models

# Create your models here.
class Profile(models.Model):
    bio = models.TextField(blank=True, default="")
    