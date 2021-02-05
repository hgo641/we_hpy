from django.db import models

# Create your models here.
class Message(models.Model):
    messagenumber = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)
    message = models.TextField()
