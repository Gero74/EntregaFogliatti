# Generated by Django 4.1.3 on 2022-12-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFogliatti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('correo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
    ]
