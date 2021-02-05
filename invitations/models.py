from django.db import models

# Create your models here.
class Invitation(models.Model):
    invitation_number = models.CharField(max_length=50)
    userID = models.CharField(max_length=50)
    studyroon_number = models.CharField(max_length=50)
    message = models.TextField()