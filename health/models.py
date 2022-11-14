from django.db import models
from pet.models import Pet
from vaccine.models import Vaccine


class Health(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet.name
