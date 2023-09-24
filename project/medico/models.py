from django.db import models
from django.db.models import Avg

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=255)

    class Meta:
        ordering = ['especialidad']
        verbose_name_plural = 'especialidades'

    def __str__(self):
        return self.especialidad


class ObraSocial(models.Model):
    obra_social = models.CharField(max_length=255)

    class Meta:
        ordering = ['obra_social']
        verbose_name_plural = 'Obras Sociales'

    def __str__(self):
        return self.obra_social
    

class Medico(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_rating(self):
        if self.reviews != None:
            return self.reviews.aggregate(Avg('score'))['score__avg']
        else:
            return None
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return ' '.join([self.name, self.surname])
    
    def save(self, *args, **kwargs):
        super(Medico, self).save(*args, **kwargs)
        if self.pk:
            self.rating = self.get_rating()


class RelMedicoEspecialidad(models.Model):
    especialidad = models.ForeignKey(Especialidad, related_name='especialidades', on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, related_name='medicos_especialidad', on_delete=models.CASCADE)

    class Meta:
        ordering = ['especialidad', 'medico']
        verbose_name_plural = 'Relaciones Medico-Especialidad'


class RelMedicoObraSocial(models.Model):
    obra_social = models.ForeignKey(ObraSocial, related_name='obras_sociales', on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, related_name='medicos_obra', on_delete=models.CASCADE)

    class Meta:
        ordering = ['obra_social', 'medico']
        verbose_name_plural = 'Relaciones Medico-Obra Social'


class Review(models.Model):
    class ScoreOptions(models.IntegerChoices):
        MUY_MALO = 1, 'Muy malo'
        MALO = 2, 'Malo'
        REGULAR = 3, 'Regular'
        BUENO = 4, 'Bueno'
        MUY_BUENO = 5, 'Muy bueno'

    score = models.PositiveSmallIntegerField(choices=ScoreOptions.choices)
    review = models.TextField()
    medico = models.ForeignKey(Medico, related_name='reviews', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        medico_obj = self.medico
        medico_obj.rating = medico_obj.get_rating()
        medico_obj.save()