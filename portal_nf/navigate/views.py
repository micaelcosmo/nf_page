from django.shortcuts import render


# nomedoapp/views.py
def horarios_de_aulas(request):
    # Lógica para recuperar os dados dos horários de aulas (você pode adaptar isso conforme sua necessidade)
    horarios = [
        {'dia': 'Segunda', 'horario': '14:00 - 16:00', 'disciplina': 'Dança Contemporânea'},
        # Adicione mais horários aqui
    ]
    return render(request, 'horarios.html', {'horarios': horarios})
