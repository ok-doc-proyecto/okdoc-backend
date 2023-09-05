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
    

class Medico(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    especialidad = models.ForeignKey(Especialidad, related_name='medicos', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('score'))['score__avg']
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return ' '.join([self.name, self.surname])
    

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