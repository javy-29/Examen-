# Generated by Django 2.0 on 2018-12-07 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField(verbose_name='Hora Inicio')),
                ('hora_termino', models.TimeField(verbose_name='Hora Termino')),
                ('id_ascensor', models.CharField(max_length=20, verbose_name='Identificador Ascensor')),
                ('modelo_ascensor', models.CharField(max_length=30, verbose_name='Model Ascensor')),
                ('fallas_detectadas', models.TextField(blank=True)),
                ('reparaciones', models.TextField(blank=True)),
                ('piezas', models.TextField(blank=True)),
                ('Cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=12)),
                ('Cliente', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='apps.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='Tecnico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps.Tecnico'),
        ),
    ]
