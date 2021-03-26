from django.db import models

# Create your models here.
class Application(models.Model):
    studyroomId = models.ForeignKey(
        "studyrooms.studyroom",
        on_delete = models.CASCADE,
        related_name = "application",)
    
    userId = models.ForeignKey(
        "users.user",
        on_delete = models.CASCADE,
        related_name = "application",)
    
    text = models.TextField()

    class AcceptanceChoices(models.TextChoices):
        Waiting = ("W", "Waiting")
        No = ("N", "No")
        Yes = ("Y","Yes")
    Acceptance = models.CharField(
        max_length=1, choices=AcceptanceChoices.choices, default = "W")