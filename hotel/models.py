from django.db import models

# Create your models here.
class Habitacion(models.Model):
    TIPO_CHOICES = [
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
    ]

    numero = models.IntegerField(unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='individual')
    descripcion = models.TextField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo}'