# Generated by Django 2.1.3 on 2018-11-30 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apiexm', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('PassUser', models.CharField(max_length=255)),
                ('Nombre', models.CharField(max_length=255)),
                ('Apellido', models.CharField(max_length=255)),
                ('Email', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
