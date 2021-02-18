from django.db import models


class Studyroom_status(models.Model):
    studyroom_number = models.AutoField(primary_key=True)
    studyroom_classification = models.CharField(max_length=64)
    studyroom_name = models.CharField(max_length=64)
    studyroom_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.studyroom_name

    class Meta:
        abstract = True


class Study_book(models.Model):
    studybook_number = models.AutoField(primary_key=True)
    writter = models.ForeignKey("users.User")
    contents = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Study_book"


class Notice_board(models.Model):
    board_number = models.AutoField(primary_key=True)
    writter = models.ForeignKey("users.User")
    contents = models.CharField(max_length=300)
    type = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "notice_board"


class Progress_rate(models.Model):
    rate_number = models.AutoField(primary_key=True)
    User = models.ForeignKey("users.User")
    progress_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "progress_rate"


class Study_time(models.Model):
    studytime_number = models.AutoField(primary_key=True)
    User = models.ForeignKey("users.User")
    study_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "study_time"


# Create your models here.
class Studyroom(Studyroom_status):  # 상속 받아서 사용
    leader_Id = models.ForeignKey(
        "users.user",
        on_delete=models.CASCADE,
        related_name="study_rooms",  # 이부분 질문
    )

    study_book = models.ManyToManyField(
        "Study_book", blank=True, related_name="study_rooms")
    notice_board = models.ManyToManyField(
        "Notice_board", blank=True, related_name="study_rooms")
    progress_rate = models.ManyToManyField(
        "Progress_rate", blank=True, related_name="study_rooms")
    study_time = models.ManyToManyField(
        "Study_time", blank=True, related_name="study_rooms")

    def __str__(self):
        return self.studyroom_name

    class Meta:
        db_table = 'Studyroom'
        verbose_name = 'Studyroom'
        verbose_name_plural = 'Studyroom'
