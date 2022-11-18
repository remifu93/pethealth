from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    username = None
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)

    class Gender(models.TextChoices):
        MALE = 'MA', 'Male'
        FEMALE = 'FE', 'Female'
        UNDEFINED = 'UN', 'Undefined'
        OTHER = 'OT', 'Other'

    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
    )

    birth_date = models.DateField()
    phone = models.CharField(max_length=22)
    id_number = models.CharField(max_length=10, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
