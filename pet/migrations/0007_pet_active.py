# Generated by Django 4.1.3 on 2022-11-14 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_alter_pet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
