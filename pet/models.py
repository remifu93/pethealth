from django.db import models
from base.models import TimeStampedModel
from user.models import User


class Pet(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)
    birth_date = models.DateField()
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    # specie
    # type(breed)

    def __str__(self):
        return self.name
