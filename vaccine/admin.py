from django.contrib import admin
from .models import Vaccine, Vaccination


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass


@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    pass
