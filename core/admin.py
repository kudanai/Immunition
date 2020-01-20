from django.contrib import admin
from .models import *

# Register your models here.


class ImmunityAdmin(admin.TabularInline):
    model = Vaccination


@admin.register(Rayyith)
class RayyithAdmin(admin.ModelAdmin):
    inlines = [ImmunityAdmin,]
    list_display = ["id_number","name", "address"]


@admin.register(ScheduleItem)
class SchedulItemAdmin(admin.ModelAdmin):
    pass