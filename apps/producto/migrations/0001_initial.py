# Generated by Django 2.2.6 on 2019-10-04 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artículo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_art', models.CharField(max_length=50)),
                ('talla', models.CharField(max_length=3)),
                ('color', models.CharField(max_length=10)),
                ('fecha_llegada', models.DateField()),
            ],
        ),
    ]
