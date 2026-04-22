from django.db import models

from django.db import models

class Hobbies(models.Model):
  id = models.IntegerField(primary_key=True)
  hobby_name = models.CharField(max_length=255)
  priority =models.IntegerField()
  weekly_hours = models.IntegerField()
  description = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Schedule(models.Model):
  id = models.IntegerField(primary_key=True)
  day_of_week = models.CharField(max_length=255)
  start_time = models.TimeField()
  end_time = models.TimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  
    
    
   
