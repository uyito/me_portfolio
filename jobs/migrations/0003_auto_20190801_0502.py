# Generated by Django 2.2.1 on 2019-08-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='about',
            field=models.CharField(max_length=300),
        ),
    ]
