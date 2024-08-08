from django import forms
from .models import Schedules, ExperimentalClass


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


class ExperimentalClassForm(forms.ModelForm):
    class Meta:
        model = ExperimentalClass
        fields = ['name', 'email', 'phone', 'weekly_day', 'level', 'start_hour', 'end_hour','modality']
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'phone': 'Telefone',
            'weekly_day': 'Dia da Semana',
            'level': 'Nível',
            'start_hour': 'Hora de Início',
            'end_hour': 'Hora de Fim',
            'modality': 'Modalidade',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome do aluno', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail do aluno', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefone do aluno', 'class': 'form-control'}),
            'weekly_day': forms.TextInput(attrs={'placeholder': 'Dia da semana', 'class': 'form-control'}),
            'level': forms.TextInput(attrs={'placeholder': 'Nível', 'class': 'form-control'}),
            'start_hour': forms.TimeInput(attrs={'placeholder': 'Hora de início', 'class': 'form-control'}),
            'end_hour': forms.TimeInput(attrs={'placeholder': 'Hora de fim', 'class': 'form-control'}),
            'modality': forms.TextInput(attrs={'placeholder': 'Modalidade', 'class': 'form-control'}),
        }
