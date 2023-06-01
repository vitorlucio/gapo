from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Conta

def doacao(request):
    conta = Conta.objects.first()
    print(conta.qrCode, '', conta.chave_pix)
    return render(request, "doacao.html", {"conta": conta})