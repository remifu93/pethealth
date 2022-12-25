from django.db import models
from user.models import User


class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Veterinario')

    class Day(models.TextChoices):
        MONDAY = 'MO', 'Lunes'
        TUESDAY = 'TU', 'Martes'
        WEDNESDAY = 'WE', 'Miercoles'
        THURSDAY = 'TH', 'Jueves'
        FRIDAY = 'FR', 'Viernes'
        SATURDAY = 'SA', 'Sabado'
        SUNDAY = 'SU', 'Domingo'

    day = models.CharField(
        'Dia',
        max_length=2,
        choices=Day.choices,
    )

    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.day} - de {self.start_time} a {self.end_time}'
