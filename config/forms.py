from django import forms
from users.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'gender']
        # 아이디와 비밀번호
        # widgets = {
        #     'email': forms.TextInput(attrs={'class': 'main__login__form__input'}),
        #     # 'gender': forms.Textarea(attrs={'class': 'login__element'}),
        # }
        labels = {
            'email': '아이디',
            'password': '비밀번호',
        }