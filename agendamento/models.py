from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.email