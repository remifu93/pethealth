# Generated by Django 4.1.3 on 2022-11-14 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_alter_pet_user'),
        ('health', '0003_remove_health_vaccines'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='pet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pet.pet'),
        ),
    ]