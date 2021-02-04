from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        OTHER = ("other", "Other")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50) 
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=1,choices = GenderChoices)
    birth = models.CharField(max_length=50)
    
