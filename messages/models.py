from django.db import models

# Create your models here.
class Message(models.Model):
    messagenumber = models.IntegerField(default=1)
    userID = models.CharField(max_length=50)
    message = models.TextField()
