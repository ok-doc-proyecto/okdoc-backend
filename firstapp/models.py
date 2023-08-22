from django.db import models

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=255)

    class Meta:
        ordering = ['especialidad']
        verbose_name_plural = 'especialidades'

    def __str__(self):
        return self.especialidad
    

class Medico(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return ' '.join([self.name, self.surname])