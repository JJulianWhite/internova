# Generated by Django 3.2.5 on 2021-07-22 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrApp', '0008_auto_20210721_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_plan', models.DateField(verbose_name='Fecha')),
                ('nombre_plan', models.CharField(max_length=100, verbose_name='Nombre Plan')),
                ('valor_plan', models.IntegerField(verbose_name='Valor Plan')),
                ('estado_plan', models.CharField(choices=[('Activo', 'Activo'), ('En proceso', 'En proceso'), ('Cerrado', 'Cerrado')], max_length=20)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
                'ordering': ['fecha_plan'],
            },
        ),
        migrations.AlterField(
            model_name='estadoinstalacion',
            name='id_instalacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.instalacion', verbose_name='Instalación'),
        ),
        migrations.CreateModel(
            name='planInstalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_planInstalacion', models.DateField(verbose_name='Fecha')),
                ('id_instalacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.instalacion', verbose_name='Instalación')),
                ('id_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.plan', verbose_name='Plan')),
            ],
            options={
                'verbose_name': 'Plan Instalación',
                'verbose_name_plural': 'Planes de Instalaciones',
                'ordering': ['id_plan'],
            },
        ),
        migrations.AddField(
            model_name='instalacion',
            name='id_plan',
            field=models.ManyToManyField(blank=True, through='AdministrApp.planInstalacion', to='AdministrApp.plan', verbose_name='Plan'),
        ),
    ]
