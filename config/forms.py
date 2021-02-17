from django import forms
from users.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'gender']