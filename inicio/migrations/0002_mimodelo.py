# Generated by Django 5.1.1 on 2024-11-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_texto1', models.CharField(max_length=100)),
                ('campo_texto2', models.CharField(blank=True, max_length=100)),
                ('campo_numero', models.IntegerField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
