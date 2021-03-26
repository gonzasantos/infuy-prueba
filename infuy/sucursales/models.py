from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.mixins import FieldCacheMixin


class Sucursal(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    direccion = models.CharField(max_length=30)

    def __str__(self):
        return "Nombre: "+self.nombre+", Direccion: "+self.direccion


class Plan(models.Model):

    class TipoPlan(models.TextChoices):
        BASICO = 'BS', 'Basico'
        COMPLETO = 'CO', 'Completo'

    tipo = models.CharField(choices=TipoPlan.choices, max_length=2,
                            default=TipoPlan.BASICO)
    costo = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return "Tipo: "+self.tipo+", Costo: "+str(self.costo)


class Afiliado(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)

    def __str__(self):
        return "Nombre: "+self.nombre+", Telefono: "+self.telefono+", Email: "+self.email


class Afiliacion(models.Model):
    descuento = models.IntegerField()
    fecha_alta = models.DateField(auto_now_add=True)
    #si se borra el plan que falle
    plan =  models.ForeignKey(Plan, on_delete=models.CASCADE)
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE)

    def __str__(self):
        return "Descuento: "+str(self.descuento)+"%"+", Fecha: "+str(self.fecha_alta)



