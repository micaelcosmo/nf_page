from django import forms
from .models import Schedules

class SchedulesForm(forms.ModelForm):
    class Meta:
        model = Schedules
        fields = '__all__'
