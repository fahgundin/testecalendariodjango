# Generated by Django 5.1.1 on 2024-12-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_calendario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registros',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
