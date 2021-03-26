from .models import Studyroom
from django import forms

class StudyroomForm(forms.ModelForm):
    class Meta:
        model = Studyroom
        fields = ['studyroom_name','studyroom_classification']
