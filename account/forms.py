from django import forms
from diaryapp.models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title','body','image']