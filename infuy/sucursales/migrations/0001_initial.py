# Generated by Django 3.1 on 2021-03-26 21:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('direccion', models.CharField(max_length=30)),
                ('ubicacion', django.contrib.gis.db.models.fields.PointField(help_text='Use map widget for point the house location', srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('BS', 'Basico'), ('CO', 'Completo')], default='BS', max_length=2)),
                ('costo', models.IntegerField()),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sucursales.sucursal')),
            ],
        ),
        migrations.CreateModel(
            name='Afiliacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descuento', models.IntegerField()),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('afiliado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sucursales.afiliado')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sucursales.plan')),
            ],
        ),
    ]
