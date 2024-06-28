# Generated by Django 5.0.6 on 2024-06-27 05:12

import django.core.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BebesYNiños',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Producto para Bebés y Niños',
                'verbose_name_plural': 'Productos para Bebés y Niños',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BebidasYLicores',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Bebida y Licor',
                'verbose_name_plural': 'Bebidas y Licores',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Carnes',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Carne',
                'verbose_name_plural': 'Carnes',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Congelados',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Producto Congelado',
                'verbose_name_plural': 'Productos Congelados',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Despensa',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Producto de Despensa',
                'verbose_name_plural': 'Productos de Despensa',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ferreteria',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Producto de Ferretería',
                'verbose_name_plural': 'Productos de Ferretería',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Limpieza',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Producto de Limpieza',
                'verbose_name_plural': 'Productos de Limpieza',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Producto para Mascotas',
                'verbose_name_plural': 'Productos para Mascotas',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PanaderiaYPasteleria',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Producto de Panadería y Pastelería',
                'verbose_name_plural': 'Productos de Panadería y Pastelería',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuesoYFiambres',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Queso y Fiambre',
                'verbose_name_plural': 'Quesos y Fiambres',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Refrigerados',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Refrigerado',
                'verbose_name_plural': 'Refrigerados',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VerdurasYFrutas',
            fields=[
                ('codigo_barra', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1)])),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('peso_producto', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1)])),
                ('fecha_elaboracion', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
            ],
            options={
                'verbose_name': 'Verdura y Fruta',
                'verbose_name_plural': 'Verduras y Frutas',
                'ordering': ['fecha_vencimiento'],
                'abstract': False,
            },
        ),
    ]
