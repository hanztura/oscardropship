from django.db import models

from modelcluster.fields import ParentalKey
from oscar.core.loading import get_model
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable

from .blocks import BannerBlock

Category = get_model('catalogue', 'Category')


class HomePage(Page):
    banner = StreamField(
        [
            ('banner', BannerBlock())
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('banner', classname='full'),
        InlinePanel('category_items', label='Category Items'),
    ]

    def get_template(request, *args, **kwargs):
        return 'uikit/home.html'


class HomePageCategory(Orderable, models.Model):
    page = ParentalKey(
        'wagtail_pages.HomePage',
        on_delete=models.CASCADE,
        related_name='category_items')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='in_home_page')

    panels = [
        FieldPanel('category')
    ]
