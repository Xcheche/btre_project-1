# Generated by Django 4.2.5 on 2025-03-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
