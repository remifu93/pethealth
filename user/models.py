from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    username = None
    first_name = models.CharField('Nombre', max_length=90)
    last_name = models.CharField('Apellido', max_length=90)

    class Gender(models.TextChoices):
        MALE = 'MA', 'Masculino'
        FEMALE = 'FE', 'Femenino'
        UNDEFINED = 'UN', 'Indefinido'
        OTHER = 'OT', 'Otro'

    gender = models.CharField(
        'Genero',
        max_length=2,
        choices=Gender.choices,
    )

    birth_date = models.DateField('Fecha de nacimiento')
    phone = models.IntegerField('Teléfono')
    id_number = models.IntegerField('Documento', unique=True)

    is_vet_user = models.BooleanField('Es Veterinario', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'birth_date', 'phone', 'id_number', ]

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email
