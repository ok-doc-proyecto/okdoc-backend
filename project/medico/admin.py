from django.contrib import admin

from .models import Especialidad, Medico, RelMedicoEspecialidad, Review

# Register your models here.
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(RelMedicoEspecialidad)
admin.site.register(Review)