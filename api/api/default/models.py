from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
=======
from django.utils import timezone

# Create your models here.
class ToDo(models.Model):
>>>>>>> aaefb09 (Made some changes)
    name = models.CharField(max_length=300, default="")
    description = models.TextField(default='')
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
