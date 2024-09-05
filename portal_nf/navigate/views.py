from .models import Schedules, ExperimentalClass
from .forms import (
    SchedulesForm, ExperimentalClassForm, ExperimentalClassesForm
    )

from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

import mercadopago


def index(request):
    """
    Renderiza a página inicial do site.

    Args:
        request (HttpRequest): A requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página inicial renderizada.
    """
    return render(request, 'index.html', {'user': request.user})

def class_schedules(request):
    """
    Renderiza a página de horários de aulas.

    Args:
        request (HttpRequest): A requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de horários de aulas renderizada.
    """
    class_schedules = Schedules.objects.all()
    return render(request, 'class_schedules.html', {'class_schedules': class_schedules})

#TODO
@login_required
def experimental_classes_management(request):
    """
    Renderiza a página de turmas experimentais.

    Args:
        request (HttpRequest): A requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de turmas experimentais renderizada.
    """
    _experimental_classes = ExperimentalClass.objects.all()
    form = ExperimentalClassesForm()
    _class_to_update = None

    if request.method == "POST":
        if 'create' in request.POST:
            form = ExperimentalClassesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('experimental_classes_management')

        elif 'update' in request.POST:
            _class_to_update = get_object_or_404(ExperimentalClass, pk=request.POST.get('schedule_id'))
            form = ExperimentalClassesForm(request.POST, instance=_class_to_update)
            if form.is_valid():
                form.save()
                return redirect('experimental_classes_management')

        elif 'delete' in request.POST:
            schedule_to_delete = get_object_or_404(ExperimentalClass, pk=request.POST.get('schedule_id'))
            schedule_to_delete.delete()
            return redirect('experimental_classes_management')

    elif request.method == "GET" and 'edit' in request.GET:
        _class_to_update = get_object_or_404(ExperimentalClass, pk=request.GET.get('schedule_id'))
        form = ExperimentalClassesForm(instance=_class_to_update)

    return render(request, 'experimental_class_management.html', {
        'experimental_classes': _experimental_classes,
        'form': form,
        'class_to_update': _class_to_update
    })

@login_required
def manage_class_schedules(request):
    """
    Renderiza a página de gerenciamento de horários de aulas.

    Args:
        request (HttpRequest): A requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de gerenciamento de horários de aulas renderizada.
    """
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

@login_required
def request_experimental_class(request):
    """
    Renderiza a página de solicitação de turma experimental.

    Args:
        request (HttpRequest): A requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de solicitação de turma experimental renderizada.
    """
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
    return render(request, 'request_experimental_class.html', {
        'experimental_class': _experimental_class,
        'form': form
    })

@login_required
def experimental_class(request):
    """
    Renderiza a página de turma experimental.

    Args:
        request (HttpRequest): A requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de turma experimental renderizada.
    """
    class_schedules = Schedules.objects.all()
    return render(request, 'class_schedules.html', {'class_schedules': class_schedules})

def register(request):
    """
    Renderiza a página de registro de usuário.

    Args:
        request (HttpRequest): A requisição HTTP.

    Returns:
        HttpResponse: A resposta HTTP com a página de registro de usuário renderizada.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirecione para a página inicial ou outro lugar
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
