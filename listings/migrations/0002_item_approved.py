# Generated by Django 4.2.6 on 2024-01-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]