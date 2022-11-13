from django.db import models
from pet.models import Pet
from vaccine.models import Vaccine


class Health(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccines = models.ManyToManyField(Vaccine)

    def __str__(self):
        return self.pet.name
