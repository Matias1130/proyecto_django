# Generated by Django 5.1.1 on 2024-11-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0003_perfumes'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfumes',
            name='genero',
            field=models.CharField(default='Unisex', max_length=10),
        ),
    ]