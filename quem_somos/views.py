from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import QuemSomos

def quem_somos(request):
    quem_somos = QuemSomos.objects.first()
    print(quem_somos)
    return render(request, "quem_somos.html", {"quem_somos": quem_somos})