from django.db import models
from base.models import TimeStampedModel
from pet.models import Pet


class Vaccine(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Vaccination(TimeStampedModel):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet.name
