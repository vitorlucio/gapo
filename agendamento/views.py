from django.shortcuts import render, redirect
from .models import Paciente
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages

def agendamento(request):
    
    if request.method == "GET":
        return render(request, 'agendamento.html')
    elif request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        descricao = request.POST.get("descricao")

        paciente = Paciente(
            nome = nome,
            email = email,
            telefone = telefone,
            descricao = descricao
        )

        paciente.save()
        messages.add_message(request, constants.SUCCESS, "Dados enviados com sucesso para o GAPO. Aguarde o contato no seu whatsapp")
        return redirect(reverse('agendamento'))


