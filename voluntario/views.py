from django.shortcuts import render, redirect
from .models import Voluntario
from django.urls import reverse
from django.contrib.messages import constants
from django.contrib import messages

def voluntario(request):
    
    if request.method == "GET":
        return render(request, 'voluntario.html')
    elif request.method == "POST":
        nome = request.POST.get("nome")
        data_nascimento = request.POST.get("data_nascimento")
        genero = request.POST.get("genero")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")

        voluntario = Voluntario(
            nome = nome,
            data_nascimento = data_nascimento,
            genero = genero,
            email= email,
            telefone = telefone,
            endereco = endereco
        )

        voluntario.save()
        messages.add_message(request, constants.SUCCESS, "Dados enviados com sucesso para o GAPO. Aguarde o contato no seu whatsapp")
        return redirect(reverse('voluntario'))


