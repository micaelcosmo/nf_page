from .models import Schedules, ExperimentalClass
from .forms import SchedulesForm, ExperimentalClassForm

from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

import mercadopago


def index(request):
    return render(request, 'index.html', {'user': request.user})

def class_schedules(request):
    class_schedules = Schedules.objects.all()
    return render(request, 'class_schedules.html', {'class_schedules': class_schedules})

def manage_class_schedules(request):
    schedules = Schedules.objects.all()
    form = SchedulesForm()
    schedule_to_update = None

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

def experimental_class(request):
    _experimental_class = ExperimentalClass.objects.all()
    form = ExperimentalClassForm()
    if request.method == 'POST':
        if 'create' in request.POST:
            form = ExperimentalClassForm(request.POST)
            if form.is_valid():
                form.save()  # Salve os dados no banco de dados
                return redirect('index')
    else:
        form = ExperimentalClassForm()
    return render(request, 'experimental_class.html', {
        'experimental_class': _experimental_class,
        'form': form
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirecione para a página inicial ou outro lugar
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
