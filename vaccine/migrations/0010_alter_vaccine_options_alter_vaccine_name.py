# Generated by Django 4.1.3 on 2022-12-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0009_remove_vaccine_expiration_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaccine',
            options={'verbose_name': 'Vacuna', 'verbose_name_plural': 'Vacunas'},
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
