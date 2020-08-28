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


class AuthorityItem(models.Model):
    name = models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True)
    image_link = models.URLField(blank=True)
    height = models.CharField(max_length=10, blank=True)
    width = models.CharField(max_length=10, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('link'),
        FieldPanel('image_link'),
        FieldPanel('height'),
        FieldPanel('width'),
    ]

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @property
    def image(self):
        return self.image_link


class SocialMediaAbstractModel(models.Model):
    twitter_handle = models.CharField(max_length=50, blank=True)
    facebook_username = models.CharField(max_length=50, blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        abstract = True

    @property
    def twitter_url(self):
        if self.twitter_handle:
            return 'https://twitter.com/' + self.twitter_handle
        else:
            return ''

    @property
    def facebook_url(self):
        if self.facebook_username:
            return 'https://facebook.com/' + self.facebook_username
        else:
            return ''

    @property
    def messenger_url(self):
        if self.facebook_username:
            return 'https://m.me/' + self.facebook_username
        else:
            return ''
