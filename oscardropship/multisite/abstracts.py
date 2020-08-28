from django.db import models

from oscar.core.loading import get_model
from wagtail.admin.edit_handlers import (
    FieldPanel, PageChooserPanel, MultiFieldPanel)

Category = get_model('catalogue', 'Category')


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete="models.CASCADE",
        null=True,
        blank=True,
        related_name='+'
    )
    link_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_category:
            return self.link_category.get_absolute_url()
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        FieldPanel('link_category'),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True
