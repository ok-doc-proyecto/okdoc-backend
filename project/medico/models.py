from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.db.models import Avg

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['especialidad']
        verbose_name_plural = 'especialidades'

    def __str__(self):
        return self.especialidad


class Prepaga(models.Model):
    prepaga = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['prepaga']
        verbose_name_plural = 'Prepagas'

    def __str__(self):
        return self.prepaga
    

class Medico(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    date_added = models.DateTimeField(auto_now_add=True)

    especialidades = models.ManyToManyField(Especialidad)
    prepagas = models.ManyToManyField(Prepaga)
    
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])
    
    def get_rating(self):
        if self.reviews != None:
            return self.reviews.aggregate(Avg('score'))['score__avg']
        else:
            return None

    def save(self, *args, **kwargs):
        super(Medico, self).save(*args, **kwargs)
        if self.pk:
            self.rating = self.get_rating()


class AccountsManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, password, **otros):
        
        otros.setdefault('is_staff', True)
        otros.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, password, **otros)

    def create_user(self, email, first_name, last_name, password, **otros):
        if not email:
            raise ValueError('You must provide an email.')
        if not first_name:
            raise ValueError('You must provide an first_name.')
        if not last_name:
            raise ValueError('You must provide an last_name.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **otros)
        user.set_password(password)
        user.save()
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_birth = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    prepagas = models.ManyToManyField(Prepaga)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountsManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


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
    usuario = models.ForeignKey(Usuario, related_name='reviews', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        medico_obj = self.medico
        medico_obj.rating = medico_obj.get_rating()
        medico_obj.save()