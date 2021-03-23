from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, MyPage


# @receiver(post_save, sender=User)
# def user_post_save(sender, **kwargs):
#    mypages = kwargs['instance'].mypages
#    mypages.save()
