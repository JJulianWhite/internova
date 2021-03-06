# Generated by Django 3.2.5 on 2021-07-21 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrApp', '0004_auto_20210721_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='aporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aporte', models.DateField(verbose_name='Fecha')),
                ('valor_aporte', models.IntegerField(verbose_name='Valor')),
                ('obs_aporte', models.TextField(verbose_name='Observación')),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.cliente', verbose_name='Nombre Socio')),
            ],
        ),
    ]
