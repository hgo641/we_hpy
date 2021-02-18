from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    # username email birth_date gender
    #username = models.CharField(max_length=50)
    class GenderChoices(models.TextChoices):
        MALE = ("m", "Male")
        FEMALE = ("f", "Female")
        OTHER = ("o", "Other")
    email = models.EmailField(max_length=254)
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices)
    birth_date = models.DateField(verbose_name=('birth_date'),null = True)


class MyPage(models.Model):
    # nickname  my_calender
    userId = models.OneToOneField("User", on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        blank=True, upload_to="user/image/%Y/%m/%d", height_field=None, width_field=None, max_length=None)
    make_study = models.ManyToManyField(
        "studyrooms.Studyroom", related_name="leaderpages")
    study_room = models.ManyToManyField(
        "studyrooms.Studyroom", related_name="mypages")
