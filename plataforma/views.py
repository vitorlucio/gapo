from django.shortcuts import render
from django.http import HttpResponse
from .models import Imovei, Cidade, Eventos
from django.shortcuts import get_object_or_404


def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    cidades = Cidade.objects.all()
    eventos = Eventos.objects.all()
    if preco_minimo or preco_maximo or cidade or tipo:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C']
        
        
        imoveis = Imovei.objects.filter(valor__gte=preco_minimo)\
        .filter(valor__lte=preco_maximo)\
        .filter(tipo_imovel__in=tipo).filter(cidade=cidade)
    else:
        imoveis = Imovei.objects.all()
    
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades, 'eventos': eventos})

def evento(request, id):
    #imovel = get_object_or_404(Imovei, id=id)
    evento = get_object_or_404(Eventos, id=id)
    sugestoes = Eventos.objects.exclude(id=id)[:2]
    return render(request, 'imovel.html', {'sugestoes': sugestoes, 'id': id, 'evento': evento})