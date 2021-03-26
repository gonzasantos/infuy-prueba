from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Sucursal)
admin.site.register(Afiliacion)
admin.site.register(Plan)
admin.site.register(Afiliado)

