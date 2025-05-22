from django import forms
from .models import Schedules, ExperimentalClass, Teacher, DanceStyle

class SchedulesForm(forms.ModelForm):
    class Meta:
        model = Schedules
        fields = ['name', 'weekly_day', 'level', 'start_hour', 'end_hour', 'status', 'teacher', 'dance_style', 'price']
        labels = {
            'name': 'Nome',
            'weekly_day': 'Dia da Semana',
            'level': 'Nível',
            'start_hour': 'Hora de Início',
            'end_hour': 'Hora de Fim',
            'status': 'Situação/Status',
            'teacher': 'Professor(a)',
            'dance_style': 'Estilo de Dança',
            'price': 'Preço',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome da aula', 'class': 'form-control'}),
            'weekly_day': forms.Select(choices=[
                ('Segunda', 'Segunda-feira'),
                ('Terça', 'Terça-feira'),
                ('Quarta', 'Quarta-feira'),
                ('Quinta', 'Quinta-feira'),
                ('Sexta', 'Sexta-feira'),
                ('Sábado', 'Sábado'),
                ('Domingo', 'Domingo'),
            ], attrs={'class': 'form-control'}),
            'level': forms.Select(choices=[
                ('Iniciante', 'Iniciante'),
                ('Intermediário', 'Intermediário'),
                ('Avançado', 'Avançado'),
            ], attrs={'class': 'form-control'}),
            'start_hour': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_hour': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'status': forms.Select(choices=[
                ('Ativa', 'Ativa'),
                ('Inativa', 'Inativa'),
                ('Férias', 'Férias'),
            ], attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'dance_style': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
        }

class ExperimentalClassForm(forms.ModelForm):
    class Meta:
        model = ExperimentalClass
        fields = ['name', 'email', 'phone', 'weekly_day', 'level', 'start_hour', 'end_hour', 'modality', 'dance_style']
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'phone': 'Telefone',
            'weekly_day': 'Dia da Semana',
            'level': 'Nível',
            'start_hour': 'Hora de Início',
            'end_hour': 'Hora de Fim',
            'modality': 'Modalidade',
            'dance_style': 'Estilo de Dança',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu@email.com', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '(XX) XXXXX-XXXX', 'class': 'form-control'}),
            'weekly_day': forms.Select(choices=[
                ('Segunda', 'Segunda-feira'),
                ('Terça', 'Terça-feira'),
                ('Quarta', 'Quarta-feira'),
                ('Quinta', 'Quinta-feira'),
                ('Sexta', 'Sexta-feira'),
                ('Sábado', 'Sábado'),
                ('Domingo', 'Domingo'),
            ], attrs={'class': 'form-control'}),
            'level': forms.Select(choices=[
                ('Iniciante', 'Iniciante'),
                ('Intermediário', 'Intermediário'),
                ('Avançado', 'Avançado'),
            ], attrs={'class': 'form-control'}),
            'start_hour': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_hour': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'modality': forms.Select(choices=[
                ('Dança do Ventre', 'Dança do Ventre'),
                ('Tribal Fusion', 'Tribal Fusion'),
            ], attrs={'class': 'form-control'}),
            'dance_style': forms.Select(attrs={'class': 'form-control'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'bio', 'specialty', 'photo_url', 'active']
        labels = {
            'name': 'Nome',
            'bio': 'Biografia',
            'specialty': 'Especialidade',
            'photo_url': 'URL da Foto',
            'active': 'Ativo',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_url': forms.URLInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class DanceStyleForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['name', 'description', 'level_description']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'level_description': 'Descrição dos Níveis',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'level_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }