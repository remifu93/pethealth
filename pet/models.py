from django.db import models
from user.models import User


class Pet(models.Model):
    name = models.CharField('Nombre', max_length=50)
    birth_date = models.DateField()
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
