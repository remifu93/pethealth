# Generated by Django 4.1.3 on 2022-12-08 15:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0002_alter_race_options_alter_race_name_alter_race_specie'),
        ('pet', '0008_pet_created_pet_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name': 'Mascota', 'verbose_name_plural': 'Mascotas'},
        ),
        migrations.AddField(
            model_name='pet',
            name='race',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='race.race', verbose_name='Raza'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='sex',
            field=models.CharField(choices=[('ML', 'Macho'), ('FM', 'Hembra')], default='FM', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='weight',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='birth_date',
            field=models.DateField(verbose_name='Fecha de nacimiento'),
        ),
    ]
