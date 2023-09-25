from django.contrib import admin

from .models import Especialidad, ObraSocial, Medico, Review, RelMedicoEspecialidad, RelMedicoObraSocial, Usuario

# Register your models here.
admin.site.register(Especialidad)
admin.site.register(ObraSocial)
admin.site.register(Medico)
admin.site.register(Review)

admin.site.register(RelMedicoEspecialidad)
admin.site.register(RelMedicoObraSocial)

admin.site.register(Usuario)