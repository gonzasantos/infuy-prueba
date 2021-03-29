import sys
from django.contrib.auth.models import Group, User
from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from .models import Afiliacion, Plan, Afiliado, Sucursal


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Plan)
admin.site.register(Afiliado)

admin.site.site_header = 'Inufy'

@admin.register(Sucursal)
class SucursalAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('nombre', 'ubicacion')
    change_list_template = "admin/mapa/mapa_change_list.html"
    default_lat = -4150239.586610202
    default_lon = -6251133.688222699
    default_zoom = 12
    list_per_page = sys.maxsize


@admin.register(Afiliacion)
class AfiliacionAdmin(admin.ModelAdmin):
    list_display = ('descuento', 'fecha_alta', 'plan', 'afiliado', 'costo_afiliacion')
