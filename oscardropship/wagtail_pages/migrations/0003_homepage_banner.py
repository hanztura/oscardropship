# Generated by Django 2.2.15 on 2020-08-26 20:22

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_pages', '0002_homepagecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner',
            field=wagtail.core.fields.StreamField([('banner', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('title_tag', wagtail.core.blocks.ChoiceBlock(choices=[('h1', 'h1'), ('p', 'p'), ('h2', 'h2'), ('h3', 'h3'), ('h4', 'h4'), ('h5', 'h5'), ('h6', 'h6')])), ('cta_text', wagtail.core.blocks.CharBlock(help='Call to Action - Text', required=False)), ('cta_href', wagtail.core.blocks.CharBlock(default='#', help='Call to Action - Target Link', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], blank=True, null=True),
        ),
    ]