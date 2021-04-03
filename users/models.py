from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from studyrooms.models import *

# Create your models here.


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("m", "Male")
        FEMALE = ("f", "Female")
        OTHER = ("o", "Other")
    email = models.EmailField(max_length=254)
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices)
    birth_date = models.DateField(verbose_name=('birth_date'), null=True)
    profile_picture = models.ImageField(
        blank=True, upload_to="user/image/%Y/%m/%d", height_field=None, width_field=None, max_length=None)
    study_room = models.ManyToManyField(
        "studyrooms.Studyroom", related_name="users")


