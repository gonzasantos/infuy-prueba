## Descripcion del proyecto
Para realizar este proyecto utilice de base Python con Django con el cual cree una solucion para gestionar sucursales.

El sistema es un administrador en el cual se puede realizar el ABM todas las entidades: sucursales, afiiaciones, planes y afiliados.

El mismo esta integrado con postgis como motor de base de datos, que permite guardar y manejar todo lo que se refiere a geolocalozacion.

En el listado de las Sucursales se puede visualizar un mapa con con todas las sucursales que existen en la base de datos, modificando la ventana de admin de django, agregue el mapa hecho con leagletjs, cada sucursal esta indicada en el mapa con un marcador de color:
* Azul que indica las sucursales que no poseen espacio para realizar actividades al aire libre.
* Verde que indica las sucursales que poseen espacio para realizar actividades al aire libre y que el clima permite hacer deporte.
* Rojo que indica las sucursales que poseen espacio para realizar actividades al aire libre pero que el clima no permite realizar deporte a aire libre.

Al momento de cargar los marcadores el sistema consulta la api de OpenWeather e indica el color del marcador segun la respuesta de la misma.

En el listado de afiliaciones se puede visualizar el calculo del costo del plan que el afiliado va a recibir.


## Como ejecutar el proyecto
Para levantar el sistema se utiliza Docker
```
docker-compose up
```


## Uso
Para acceder a la app usar dirigirse a la siguiente pagina
http://127.0.0.1:8000/
y utilizar las siguientes credenciales:
* USERNAME: infuy
* PASSWORD: infuy


### Para correr los tests
```
docker-compose run infuy python manage.py test --keepdb
```


### Configuraciones del sistema
Se agregaron extra estas settings para configurar el uso de OpenWeather:
* `infuy.settings.OPENWEATHER_URL`: Url de la api del clima.
* `infuy.settings.OPENWEATHER_API_KEY`: Key de la api del clima.

## Cosas para mejorar

Variables de configuracion como la OPENWEATHER_API_KEY deberian ser tomadas de una variable de entorno en vez de estar hardcodeadas.
Si se quisiera agregar mas llamadas a esta api (openweather) con diferentes parametros, convendria mover las llamadas a un modulo a parte.
