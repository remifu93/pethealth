from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from base.models import TimeStampedModel
from user.models import User
from race.models import Race


class Pet(TimeStampedModel):

    class SexChoices(models.TextChoices):
        MALE = 'ML', 'Macho'
        FEMALE = 'FM', 'Hembra'

    name = models.CharField('Nombre', max_length=50)
    birth_date = models.DateField('Fecha de nacimiento')
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    active = models.BooleanField('Activo', default=True)
    race = models.ForeignKey(Race, verbose_name='Raza', on_delete=models.CASCADE)
    sex = models.CharField(
        'Sexo',
        max_length=2,
        choices=SexChoices.choices,
    )
    weight = models.SmallIntegerField(
        'Peso',
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return self.name
