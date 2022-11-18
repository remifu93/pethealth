from specie.models import Specie
from django.db import models


class Race(models.Model):
    specie = models.ForeignKey(Specie, verbose_name='Especie', on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

    def __str__(self):
        return self.name
