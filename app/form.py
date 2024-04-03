from django.forms import ModelForm
from .models import DailyDiary

class DailyDiaryForm(ModelForm):
    class Meta:
        model = DailyDiary
        fields = ["title","content"]
