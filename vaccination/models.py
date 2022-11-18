from django.db import models
from base.models import TimeStampedModel
from pet.models import Pet
from vaccine.models import Vaccine


class Vaccination(TimeStampedModel):
    pet = models.ForeignKey(Pet, verbose_name='Mascota', on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, verbose_name='Vacuna', on_delete=models.CASCADE)
    date_placed = models.DateField('Fecha colocación')
    active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = "Vacunación"
        verbose_name_plural = "Vacunaciones"

    def __str__(self):
        return self.pet.name
