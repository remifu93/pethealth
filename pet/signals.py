from django.db.models.signals import post_save
from django.dispatch import receiver
from health.models import Health
from .models import Pet


@receiver(post_save, sender=Pet)
def create_pet_health_profile(sender, instance, created, **kwargs):
    print("signal pre create")
    if created:
        print("signal created")
        Health.objects.create(pet=instance)