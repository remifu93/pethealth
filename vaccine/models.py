from django.db import models
from base.models import TimeStampedModel


class Vaccine(TimeStampedModel):
    name = models.CharField(max_length=50)
    # expiration_date

    def __str__(self):
        return self.name
