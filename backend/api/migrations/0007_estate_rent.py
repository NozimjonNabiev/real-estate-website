# Generated by Django 5.0 on 2024-01-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_contracts_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='rent',
            field=models.BooleanField(default=False),
        ),
    ]
