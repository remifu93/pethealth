from django.contrib import admin
from .models import Specie


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    pass
