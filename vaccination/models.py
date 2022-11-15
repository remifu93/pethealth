from django.db import models
from base.models import TimeStampedModel
from pet.models import Pet
from vaccine.models import Vaccine


class Vaccination(TimeStampedModel):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_placed = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.pet.name
