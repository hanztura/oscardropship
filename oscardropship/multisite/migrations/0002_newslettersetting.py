# Generated by Django 2.2.15 on 2020-08-27 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20190918_0122'),
        ('wagtailcore', '0052_pagelogentry'),
        ('multisite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_newsletter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletter.Newsletter')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
