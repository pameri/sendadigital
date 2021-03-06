# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fregistro', models.DateTimeField(auto_now_add=True)),
                ('tipodoi', models.EmailField(max_length=254)),
                ('nrodoi', models.CharField(blank=True, max_length=11, null=True)),
                ('razonsocial', models.CharField(blank=True, max_length=150, null=True)),
                ('direfiscal', models.CharField(blank=True, max_length=250, null=True)),
                ('pais', models.CharField(default='PE', max_length=2)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fregistro', models.DateTimeField(auto_now_add=True)),
                ('pedido', models.CharField(max_length=250)),
                ('contacto', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=100)),
                ('informacion', models.TextField(blank=True, null=True)),
                ('estado_contrato', models.CharField(max_length=1)),
                ('estado', models.CharField(max_length=1)),
                ('url_factura', models.CharField(max_length=250)),
                ('entidad', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Entidad')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fregistro', models.DateTimeField(auto_now_add=True)),
                ('tipopersona', models.CharField(max_length=1)),
                ('tipodoi', models.CharField(max_length=1)),
                ('nrodoi', models.CharField(blank=True, max_length=11, null=True)),
                ('razonsocial', models.CharField(blank=True, max_length=250, null=True)),
                ('direfiscal', models.CharField(blank=True, max_length=250, null=True)),
                ('pais', models.CharField(default='PE', max_length=2)),
                ('departamento', models.CharField(blank=True, max_length=250, null=True)),
                ('provincia', models.CharField(blank=True, max_length=250, null=True)),
                ('distrito', models.CharField(blank=True, max_length=250, null=True)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('informacion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fregistro', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.CharField(max_length=5)),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('estado', models.CharField(max_length=1)),
                ('moneda', models.CharField(default='PEN', max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='perfil',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Perfil'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Producto'),
        ),
    ]
