# Generated by Django 2.2.15 on 2020-08-27 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multisite', '0002_newslettersetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersetting',
            name='default_newsletter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='newsletter.Newsletter'),
        ),
    ]
