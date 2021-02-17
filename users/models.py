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
    #userID = models.AutoField(primary_key = True)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=1,choices = GenderChoices.choices, unique = True)
    birth_date = models.CharField(max_length=50)

    


class My_page(models.Model):
    #nickname  my_calender 
    #My_pagenumber = models.AutoField(primary_key = True)
    userId = models.ForeignKey("User", on_delete=models.CASCADE, null=False, blank=False)
    profile_picture = models.ImageField(blank = True, upload_to="user/image/%Y/%m/%d", height_field=None, width_field=None, max_length=None)
    make_study = models.ManyToManyField("studyrooms.Studyroom", related_name = "make_study") 
    study_room = models.ManyToManyField("studyrooms.Studyroom", related_name = "study_room")

