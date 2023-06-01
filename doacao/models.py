from django.db import models

class Conta(models.Model):
    qrCode = models.ImageField(upload_to='img')
    chave_pix = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.chave_pix
