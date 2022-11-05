from django.db import models
# Create your models here.
class todo(models.Model):
    task = models.CharField(max_length = 100)
    date = models.DateField()
    complted = models.BooleanField(default = False)
   





class notes(models.Model):
    title = models.CharField(max_length = 100)
    notes = models.TextField()


class ideas(models.Model):
    ideas = models.CharField(max_length = 100, blank = True,null=True)

class goals(models.Model):
    goals = models.CharField(max_length = 100, blank = True,null=True)
