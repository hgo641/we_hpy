from django.db import models

# Create your models here.
class Message(models.Model):
    messagenumber = models.AutoField(primary_key=True)
    userID = models.ForeignKey(users.User, on_delete=models.CASCADE)
    message = models.TextField()
    
