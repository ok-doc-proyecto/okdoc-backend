from django.contrib import admin

from .models import Especialidad, Prepaga, Medico, Review, Usuario

# Register your models here.
admin.site.register(Especialidad)
admin.site.register(Prepaga)
admin.site.register(Medico)
admin.site.register(Review)

admin.site.register(Usuario)