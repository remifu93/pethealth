from django.db import models


class Specie(models.Model):
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"
    
    def __str__(self):
        return self.name
