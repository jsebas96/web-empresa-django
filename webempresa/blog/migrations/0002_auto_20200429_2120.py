# Generated by Django 3.0.4 on 2020-04-29 21:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
        ),
    ]
