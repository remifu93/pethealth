from django.contrib import admin
from .models import Vaccination


@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    pass
