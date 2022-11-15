from specie.models import Specie
from django.db import models


class Race(models.Model):
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
