# Generated by Django 5.0 on 2024-01-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_property_amenities_estate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
