from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Todo
class Todo(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     work = models.TextField()
     start = models.DateTimeField()
     finish = models.DateTimeField()
     status = models.BooleanField(default=False)
     def __str__(self):
          return self.work