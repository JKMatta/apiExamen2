# Generated by Django 2.1.3 on 2018-12-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiexm', '0014_auto_20181201_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Email',
            field=models.CharField(max_length=255),
        ),
    ]
