from django.contrib import admin
from .models import Vaccine


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass

