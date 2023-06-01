from django.db import models

class Voluntario(models.Model):
    OPCOES_GENERO = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino')
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=2, null=False, blank=False, choices=OPCOES_GENERO)
    email = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
 
    def __str__(self) -> str:
        return self.email