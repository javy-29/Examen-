from django.db import models
from django.utils import timezone

# Create your models here.
class Tecnico(models.Model):
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    Cliente = models.ForeignKey('apps.Cliente', on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
  

    def __str__(self):
        return self.nombre

    
    
class Orden(models.Model):
    Cliente = models.ForeignKey('apps.Cliente', blank=True, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField(verbose_name="Hora Inicio")
    hora_termino = models.TimeField(verbose_name="Hora Termino")
    id_ascensor = models.CharField(max_length=20, verbose_name="Identificador Ascensor")
    modelo_ascensor = models.CharField(max_length=30, verbose_name="Model Ascensor")
    fallas_detectadas = models.TextField(blank=True)
    reparaciones = models.TextField (blank=True)
    piezas = models.TextField(blank=True)
    Tecnico = models.ForeignKey('apps.Tecnico',blank=True,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_ascensor






