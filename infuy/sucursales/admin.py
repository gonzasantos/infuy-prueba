from .models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.gis import admin as geoadmin

from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Afiliacion)
admin.site.register(Plan)
admin.site.register(Afiliado)

admin.site.site_header = 'Inufy'

@admin.register(Sucursal)
class SucursalAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('nombre', 'ubicacion')
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }