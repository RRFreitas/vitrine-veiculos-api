from django.db import models
from django.core.validators import MinLengthValidator

class Carro(models.Model):
    nome = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    marca = models.CharField(max_length=200)
    ano = models.PositiveSmallIntegerField()
    km = models.PositiveIntegerField()
    estado = models.CharField(max_length=30)
    valor = models.DecimalField(decimal_places=2, max_digits=12)
    foto = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.marca} {self.nome} {self.ano} - {self.valor}"