from django.db import models
from base.models import TimeStampedModel


class Vaccine(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        verbose_name = "Vacuna"
        verbose_name_plural = "Vacunas"

    def __str__(self):
        return self.name
