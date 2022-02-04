from django.contrib import admin
from .models import Tareas


# Register your models here.

class TareasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Tareas, TareasAdmin)