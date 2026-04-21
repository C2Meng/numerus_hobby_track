from django.db import models

from django.db import models

class Hobbies(models.Model):
  hobby = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
