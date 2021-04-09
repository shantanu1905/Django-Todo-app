from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Taskdata(models.Model):
    TaskTitle = models.CharField(max_length=50)
    taskdesc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.TaskTitle

    