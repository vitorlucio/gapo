from django.db import models

class ImagemQuemSomos(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url


class QuemSomos(models.Model):
    imagens = models.ManyToManyField(ImagemQuemSomos)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.descricao
