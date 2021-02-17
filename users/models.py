from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.conf import settings
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, gender, birth_date, password):
        if not email:
            raise ValueError("Email Needed")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            gender=gender,
            birth_date=birth_date,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    # username email birth_date gender
    #username = models.CharField(max_length=50)
    class GenderChoices(models.TextChoices):
        MALE = ("m", "Male")
        FEMALE = ("f", "Female")
        OTHER = ("o", "Other")
    email = models.EmailField(max_length=254)
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices, unique=True)
    birth_date = models.DateField()
    objects = UserManager()


class My_page(models.Model):
    # nickname  my_calender
    userId = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=False, blank=False)
    profile_picture = models.ImageField(
        blank=True, upload_to="user/image/%Y/%m/%d", height_field=None, width_field=None, max_length=None)
    make_study = models.ManyToManyField(
        "studyrooms.Studyroom", related_name="make_study")
    study_room = models.ManyToManyField(
        "studyrooms.Studyroom", related_name="study_room")
