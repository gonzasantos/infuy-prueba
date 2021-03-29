import json
from unittest.result import failfast
import requests
from django.contrib.gis.db import models
from django.conf import settings


class Sucursal(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    ubicacion = models.PointField(help_text="Indique la ubicacion en el mapa")
    espacio_afuera = models.BooleanField('Dispone de espacio al aire libre', default=False)

    class Meta:
        verbose_name_plural = "Sucursales"

    @property
    def lat_lang(self):
        return [self.ubicacion.y, self.ubicacion.x]

    @property
    def disponible(self):
        if not self.espacio_afuera:
            return None

        params = {
            'lat' : self.ubicacion.y,
            'lon' : self.ubicacion.x,
            'exclude' : 'minutely,daily,alerts,hourly',
            'appid' : settings.OPENWEATHER_API_KEY,
        }
        try:
            r = requests.get(url=settings.OPENWEATHER_URL, params=params)
            weather = r.json()['weather'][0]['description']
        except(json.decoder.JSONDecodeError, KeyError, requests.exceptions.RequestException):
            return False
        if weather == 'clear sky' or weather == 'few clouds' or weather == 'scattered clouds' or weather == 'broken clouds':
            return True
        return False

    def __str__(self):
        return self.nombre

class Plan(models.Model):

    class TipoPlan(models.TextChoices):
        BASICO = 'BS', 'Basico'
        COMPLETO = 'CO', 'Completo'

    tipo = models.CharField(choices=TipoPlan.choices, max_length=2,
                            default=TipoPlan.BASICO)
    costo = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Planes"

    def __str__(self):
        return "Tipo: %s, Costo: %s" % (self.tipo, self.costo)


class Afiliado(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)

    def __str__(self):
        return "Nombre: %s, Telefono: %s, Email: %s" % (self.nombre, self.telefono, self.email)


class Afiliacion(models.Model):
    descuento = models.IntegerField()
    fecha_alta = models.DateField(auto_now_add=True)
    plan =  models.ForeignKey(Plan, on_delete=models.CASCADE)
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Afiliaciones"

    def __str__(self):
        return "Descuento: %s, Fecha: %s" % (self.descuento, self.fecha_alta)

    @property
    def costo_afiliacion(self):
        return self.plan.costo * self.descuento/100