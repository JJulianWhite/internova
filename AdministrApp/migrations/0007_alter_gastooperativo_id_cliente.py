# Generated by Django 3.2.5 on 2021-07-22 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrApp', '0006_auto_20210721_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastooperativo',
            name='id_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdministrApp.cliente', verbose_name='Cliente'),
        ),
    ]