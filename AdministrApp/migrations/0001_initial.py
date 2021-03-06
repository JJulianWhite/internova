# Generated by Django 3.2.5 on 2021-07-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cliente', models.DateField(auto_now=True)),
                ('documento_cliente', models.CharField(max_length=20, verbose_name='Número de Documento')),
                ('nombre_cliente', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido_cliente', models.CharField(max_length=100, verbose_name='Apellido')),
                ('celular_cliente', models.CharField(max_length=20, verbose_name='Número Celular')),
                ('correo_cliente', models.CharField(max_length=100, verbose_name='Correo Electónico')),
                ('genero_cliente', models.CharField(choices=[('0', 'Femenino'), ('1', 'Masculino'), ('2', 'Otros')], max_length=1, verbose_name='Género')),
                ('perfil_cliente', models.CharField(choices=[('0', 'Cliente'), ('1', 'Empleado'), ('2', 'Socio')], default=0, max_length=1, verbose_name='Perfil')),
                ('obs_cliente', models.TextField(verbose_name='Observación')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['apellido_cliente'],
            },
        ),
        migrations.CreateModel(
            name='inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_inmueble', models.CharField(max_length=20, verbose_name='Punto GPS')),
                ('direccion_inmueble', models.CharField(max_length=100, verbose_name='Dirección')),
                ('barrio_inmueble', models.CharField(choices=[('0', 'Palmas'), ('1', 'Mirador')], default=0, max_length=2, verbose_name='Barrio')),
                ('ciudad_inmueble', models.CharField(choices=[('0', 'Girón'), ('1', 'Bucaramanga')], default=0, max_length=2, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Inmueble',
                'verbose_name_plural': 'Inmuebles',
                'ordering': ['barrio_inmueble', 'direccion_inmueble'],
            },
        ),
    ]
