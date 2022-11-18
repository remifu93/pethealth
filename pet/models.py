from django.db import models
from base.models import TimeStampedModel
from user.models import User


class Pet(TimeStampedModel):
    name = models.CharField('Nombre', max_length=50)
    birth_date = models.DateField('Fecha de nacimiento')
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    active = models.BooleanField('Active', default=True)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return self.name
