import responses
import requests
from django.conf import settings
from django.test import TestCase
from django.contrib.gis.geos import Point
from requests.exceptions import ConnectionError, HTTPError
from .models import Sucursal


class TestSucursal(TestCase):
    @responses.activate
    def test_sucursal_espacio_afuera_false(self):
        """
        Test Disponible retorna None
        si no tiene espacio para hacer ejercicio al aire libre
        """
        expected_response = None
        responses.add(responses.GET, settings.OPENWEATHER_URL,
                      json=expected_response, status=200)
        suc = Sucursal.objects.create(
            nombre='sucName',
            ubicacion=Point(60.99, 30.9),
            espacio_afuera=False
        )
        assert suc.disponible is None

    @responses.activate
    def test_sucursal_diponible_true(self):
        """
        Test Disponible retorna True
        en caso de tener espacio al aire libre y que este disponible
        por el clima
        """
        expected_response = {
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "03d"
                }
            ],
        }
        responses.add(responses.GET, settings.OPENWEATHER_URL,
                      json=expected_response, status=200)
        suc = Sucursal.objects.create(
            nombre='sucName',
            ubicacion=Point(60.99, 30.9),
            espacio_afuera=True
        )
        assert suc.disponible is True


    @responses.activate
    def test_sucursal_diponible_false(self):
        """
        Test Disponible retorna False
        en caso de tener espacio al aire libre y que NO este disponible
        por el clima
        """
        expected_response = {
            "weather": [
                {
                    "id": 802,
                    "main": "Rain",
                    "description": "rain",
                    "icon": "03d"
                }
            ],
        }
        responses.add(responses.GET, settings.OPENWEATHER_URL,
                      json=expected_response, status=200)
        suc = Sucursal.objects.create(
            nombre='sucName',
            ubicacion=Point(60.99, 30.9),
            espacio_afuera=True
        )
        assert suc.disponible is False


    @responses.activate
    def test_sucursal_diponible_json_error(self):
        """
        Test Disponible retorna False
        en caso de tener espacio al aire libre y que NO este disponible
        por el clima
        """
        expected_response = """{
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": scattered clouds,
                    "icon": "03d"
                }
            ],
        }
        """
        responses.add(responses.GET, settings.OPENWEATHER_URL,
                      body=expected_response, status=200)
        suc = Sucursal.objects.create(
            nombre='sucName',
            ubicacion=Point(60.99, 30.9),
            espacio_afuera=True
        )
        assert suc.disponible is False
