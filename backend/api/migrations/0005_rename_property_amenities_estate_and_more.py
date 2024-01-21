# Generated by Django 5.0 on 2024-01-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_agents_license'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amenities',
            old_name='property',
            new_name='estate',
        ),
        migrations.RenameField(
            model_name='contracts',
            old_name='property',
            new_name='estate',
        ),
        migrations.RenameField(
            model_name='favorites',
            old_name='property',
            new_name='estate',
        ),
        migrations.AlterField(
            model_name='estate',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='estate',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]