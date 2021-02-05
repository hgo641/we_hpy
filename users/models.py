from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    #username email birth_date gender
    class GenderChoices(models.TextChoices):
        MALE = ("m", "Male")
        FEMALE = ("f", "Female")
        OTHER = ("o", "Other")
    #username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=1,choices = GenderChoices.choices, unique = True)
    birth_date = models.CharField(max_length=50)


class My_page(models.Model):
    #nickname profile_picture make_study my_calender study_room
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    profile_picture = models.ImageField(blank = True, upload_to="user/image/%Y/%m/%d", height_field=None, width_field=None, max_length=None)
    #make_study = models.ManyToManyField(Studyroom) 
    #study_room = models.ManyToManyField(Studyroom)
