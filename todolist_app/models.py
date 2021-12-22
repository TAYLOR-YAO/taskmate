from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# create Tasklist Model


class Tasklist(models.Model):
    manage = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

# Rename objects as task
    def __str__(self):
        return self.task + '-' + str(self.done)


#  the run -> python manage.py makemigrations
#  the run -> python manage.py migrate
