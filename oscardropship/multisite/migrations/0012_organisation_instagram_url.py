# Generated by Django 2.2.15 on 2020-08-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multisite', '0011_organisation_pinterest_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='instagram_url',
            field=models.URLField(blank=True),
        ),
    ]