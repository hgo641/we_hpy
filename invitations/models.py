from django.db import models

# Create your models here.
class Invitation(models.Model):
    invitation_number = models.AutoField(primary_key=True)
    userID = models.ForeignKey(users.User, on_delete=models.CASCADE)
    studyroom_number = models.ForeignKey(studyrooms.Studyroom_status, on_delete=models.CASCADE)
    message = models.TextField()

    