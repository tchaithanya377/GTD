from django.db import models
# Create your models here.
class todo(models.Model):
    task = models.CharField(max_length = 100)
    date = models.DateField()
    complted = models.BooleanField(null=True, blank = True)
    property = models.CharField(max_length = 10, blank = True,null=True)
    ideas = models.TextField(blank = True,null=True)
    goals = models.CharField(max_length = 100, blank = True,null=True)
   


class notes(models.Model):
    title = models.CharField(max_length = 100)
    notes = models.TextField()