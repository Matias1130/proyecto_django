# Generated by Django 5.1.1 on 2024-11-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_delete_cremas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=10)),
            ],
        ),
    ]
