from django.db import models

from modelcluster.fields import ParentalKey
from oscar.core.loading import get_model
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel, 
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page, Orderable

from .blocks import BannerBlock

Category = get_model('catalogue', 'Category')
Product = get_model('catalogue', 'Product')
ProductRecord = get_model('analytics', 'ProductRecord')


class HomePage(Page):
    banner = StreamField(
        [
            ('banner', BannerBlock())
        ],
        blank=True,
        null=True,
    )
    about = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('banner', classname='full'),
        FieldPanel('about', classname='full'),
        InlinePanel(
            'category_items',
            label='Category Items',
        ),
        InlinePanel(
            'special_products',
            label='Special Products',
        ),
        InlinePanel(
            'featured_products',
            label='Featured Products',
        ),
    ]

    def get_template(request, *args, **kwargs):
        return 'uikit/home.html'

    def get_most_viewed_products(self):
        queryset = ProductRecord.objects.filter(product__parent__isnull=True)
        queryset = queryset.prefetch_related('product__images')
        queryset = queryset.order_by('-num_views')[:10]
        return queryset

    def get_best_selling_products(self):
        queryset = ProductRecord.objects.filter(product__parent__isnull=True)
        queryset = queryset.prefetch_related('product__images')
        queryset = queryset.order_by('-num_purchases', '-num_views')[:10]
        return queryset

    def get_newly_arrived_products(self):
        queryset = Product.objects.browsable().filter(parent__isnull=True)
        queryset = queryset.prefetch_related('images')[:6]
        return queryset

    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context['new_arrivals'] = self.get_newly_arrived_products()
        context['most_viewed_products'] = self.get_most_viewed_products()
        context['best_selling_products'] = self.get_best_selling_products()
        return context


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


class HomePageSpecialProduct(Orderable, models.Model):
    page = ParentalKey(
        'wagtail_pages.HomePage',
        on_delete=models.CASCADE,
        related_name='special_products')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='home_page_specials')

    panels = [
        FieldPanel('product')
    ]


class HomePageFeaturedProduct(Orderable, models.Model):
    page = ParentalKey(
        'wagtail_pages.HomePage',
        on_delete=models.CASCADE,
        related_name='featured_products')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='home_page_featured')

    panels = [
        FieldPanel('product')
    ]
