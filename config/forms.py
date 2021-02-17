from django import forms
from users.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        # model = Question
        # fields = ['subject', 'content']