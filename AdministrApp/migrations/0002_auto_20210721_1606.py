# Generated by Django 3.2.5 on 2021-07-21 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo_cliente',
            field=models.EmailField(max_length=100, verbose_name='Correo Electónico'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_cliente',
            field=models.DateField(auto_now=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero_cliente',
            field=models.CharField(choices=[('0', 'Femenino'), ('1', 'Masculino'), ('2', 'Otros')], default=0, max_length=1, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='obs_cliente',
            field=models.TextField(blank=True, null=True, verbose_name='Observación'),
        ),
        migrations.CreateModel(
            name='instalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_instalacion', models.DateField(auto_now=True, verbose_name='Fecha')),
                ('nad_instalacion', models.CharField(max_length=20, verbose_name='NAD de instalación')),
                ('ip_instalacion', models.CharField(max_length=20, verbose_name='IP asignada')),
                ('valor_instalacion', models.IntegerField(default=0, verbose_name='Valor Instalación')),
                ('obs_instalacion', models.TextField(verbose_name='Observación')),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.cliente', verbose_name='Nombre cliente')),
                ('id_inmueble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.inmueble', verbose_name='Inmueble de instalación')),
            ],
        ),
    ]
