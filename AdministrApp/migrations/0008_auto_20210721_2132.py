# Generated by Django 3.2.5 on 2021-07-22 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrApp', '0007_alter_gastooperativo_id_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(choices=[('Activo', 'Activo'), ('En proceso', 'En proceso'), ('Cerrado', 'Cerrado')], max_length=20, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['nombre_estado'],
            },
        ),
        migrations.CreateModel(
            name='estadoInstalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_estadoInstalacion', models.DateField(verbose_name='Fecha')),
                ('obs_estadoInstalacion', models.TextField(verbose_name='Observacion')),
                ('id_estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.estado', verbose_name='Estado')),
                ('id_instalacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.instalacion', verbose_name='Instalacion')),
            ],
            options={
                'verbose_name': 'Estado Instalación',
                'verbose_name_plural': 'Estados de Instalaciones',
                'ordering': ['id_estado'],
            },
        ),
        migrations.AddField(
            model_name='instalacion',
            name='id_estado',
            field=models.ManyToManyField(blank=True, through='AdministrApp.estadoInstalacion', to='AdministrApp.estado', verbose_name='Estado'),
        ),
    ]
