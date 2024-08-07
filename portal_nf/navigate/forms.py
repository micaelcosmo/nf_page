from django import forms
from .models import Schedules


class SchedulesForm(forms.ModelForm):
    class Meta:
        model = Schedules
        fields = ['name', 'weekly_day', 'level', 'start_hour', 'end_hour', 'status']
        labels = {
            'name': 'Nome',
            'weekly_day': 'Dia da Semana',
            'level': 'Nível',
            'start_hour': 'Hora de Início',
            'end_hour': 'Hora de Fim',
            'status': 'Situação/Status',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da aula', 'class': 'form-control'}),
            'weekly_day': forms.TextInput(attrs={'placeholder': 'Dia da semana', 'class': 'form-control'}),
            'level': forms.TextInput(attrs={'placeholder': 'Nível', 'class': 'form-control'}),
            'start_hour': forms.TimeInput(attrs={'placeholder': 'Hora de início', 'class': 'form-control'}),
            'end_hour': forms.TimeInput(attrs={'placeholder': 'Hora de fim', 'class': 'form-control'}),
            'status': forms.TextInput(attrs={'placeholder': 'Situação/Status', 'class': 'form-control'}),
        }
