from .models import Schedules
from .forms import SchedulesForm

from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    return render(request, 'index.html')

def class_schedules(request):
    # Consulta todos os registros da tabela 'schedules'
    class_schedules = Schedules.objects.all()
    return render(request, 'class_schedules.html', {'class_schedules': class_schedules})

def manage_class_schedules(request):
    # Listar todos os schedules
    schedules = Schedules.objects.all()

    # Inicializar variáveis para o formulário e o objeto a ser deletado
    form = SchedulesForm()
    schedule_to_update = None
    schedule_to_delete = None

    # Verificar se é uma requisição POST
    if request.method == "POST":
        if 'create' in request.POST:
            form = SchedulesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage_class_schedules')

        elif 'update' in request.POST:
            schedule_to_update = get_object_or_404(Schedules, pk=request.POST.get('schedule_id'))
            form = SchedulesForm(request.POST, instance=schedule_to_update)
            if form.is_valid():
                form.save()
                return redirect('manage_class_schedules')

        elif 'delete' in request.POST:
            schedule_to_delete = get_object_or_404(Schedules, pk=request.POST.get('schedule_id'))
            schedule_to_delete.delete()
            return redirect('manage_class_schedules')

    elif request.method == "GET" and 'edit' in request.GET:
        schedule_to_update = get_object_or_404(Schedules, pk=request.GET.get('schedule_id'))
        form = SchedulesForm(instance=schedule_to_update)

    return render(request, 'management.html', {
        'schedules': schedules,
        'form': form,
        'schedule_to_update': schedule_to_update
    })
