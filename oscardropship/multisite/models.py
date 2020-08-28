from django.conf import settings
from django.db import models

from colorfield.fields import ColorField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

from .abstracts import RelatedLink


@register_setting
class FooterSettings(BaseSetting, ClusterableModel):
    """The FooterLinks model takes advantage of the RelatedLink model we
    implemented above.
    """
    about = models.TextField(blank=True)

    panels = [
        FieldPanel('about'),
        InlinePanel('footer_links', label="Footer Links"),
    ]

    @property
    def category_links(self):
        return self.footer_links.filter(
            link_category__isnull=False).select_related('link_category')

    @property
    def non_category_links(self):
        return self.footer_links.filter(link_category__isnull=True)


class FooterLinksRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('FooterSettings', related_name='footer_links')


@register_setting
class SeoSettings(BaseSetting):
    google_analytics_id = models.CharField(
        max_length=50,
        default=settings.GOOGLE_ANALYTICS_PROPERTY_ID,
        blank=True
    )
    robots_txt = models.FileField(
        upload_to='seo/')
    facebook_app_id = models.CharField(max_length=100, blank=True)
    facebook_pixel_id = models.CharField(max_length=100, blank=True)
    brand_name_in_title = models.CharField(max_length=50, blank=True)
    append_brand_name_in_title = models.BooleanField(default=True)


@register_setting
class NewsletterSetting(BaseSetting):
    default_newsletter = models.ForeignKey(
        'newsletter.Newsletter',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )


@register_setting
class SiteBranding(BaseSetting):
    """RE the SiteBranding model, you'll note that there's no
    custom-validation on the
    banner_colour field to check that a valid hex value has been
    entered. This would
    probably be better off as a select field with a set of predefined
    colour choices.
    """
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    fav_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    nav_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    primary_color = ColorField(default='#000000')
    secondary_color = ColorField(default='#000000')
    accent_color = ColorField(default='#000000')
    accent_2_color = ColorField(default='#000000')
    banner_colour = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text="Fill in a hex colour value"
    )
    css = models.FileField(
        upload_to='css/sites/',
        null=True,
        blank=True)

    panels = [
        MultiFieldPanel(
            (
                ImageChooserPanel('site_logo'),
                ImageChooserPanel('fav_icon'),
                ImageChooserPanel('nav_icon'),
            ),
            'Site Logos'
        ),
        MultiFieldPanel(
            (
                FieldPanel('primary_color'),
                FieldPanel('secondary_color'),
                FieldPanel('accent_color'),
                FieldPanel('accent_2_color'),
            ),
            'Color Palette',
        ),
        FieldPanel('css'),
    ]


@register_setting
class SocialMediaSettings(BaseSetting):
    """The SocialMediaSettings model provides site-specific social media links.
    These could be easily expanded to include any number of social media
    URLs / IDs.
    """
    facebook = models.URLField(
        help_text='Your Facebook page URL',
        null=True,
        blank=True
    )
    twitter = models.CharField(
        max_length=255,
        help_text='Your Twitter username, without the @',
        null=True,
        blank=True
    )
