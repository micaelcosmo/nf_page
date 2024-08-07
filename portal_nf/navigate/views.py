from django.shortcuts import render
from .models import Schedules


def index(request):
    return render(request, 'index.html')

def class_schedules(request):
    # Consulta todos os registros da tabela 'schedules'
    class_schedules = schedules = Schedules.objects.all()
    return render(request, 'class_schedules.html', {'class_schedules': class_schedules})
