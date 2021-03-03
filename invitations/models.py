from django.db import models

# Create your models here.


class Conversation(models.Model):

    ''' 단톡방 '''
    members = models.ManyToManyField("users.User")
    studyroom = models.OneToOneField(
        "studyrooms.Studyroom", on_delete=models.CASCADE)
    # studyroom.leader
    title = models.CharField(max_length=50)


class Message(models.Model):
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE)
    author = models.ManyToManyField("users.User", related_name="messages")
    # 유효성 검사 : members 안에 속해있어야 한다.
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
