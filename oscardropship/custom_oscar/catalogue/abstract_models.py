from oscar.apps.catalogue.abstract_models import (
    AbstractCategory as BaseAbstractCategory,
    AbstractProduct as BaseAbstractProduct,
    _,
    reverse)


class AbstractCategory(BaseAbstractCategory):
    _slug_separator = '/'

    class Meta:
        abstract = True
        app_label = 'catalogue'
        ordering = ['path']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def _get_absolute_url(self, parent_slug=None):
        """
        Our URL scheme means we have to look up the category's ancestors. As
        that is a bit more expensive, we cache the generated URL. That is
        safe even for a stale cache, as the default implementation of
        ProductCategoryView does the lookup via primary key anyway. But if
        you change that logic, you'll have to reconsider the caching
        approach.
        """
        return reverse('catalogue:category', kwargs={
            'category_slug': self.slug, 'pk': self.pk
        })


class AbstractProduct(BaseAbstractProduct):

    class Meta:
        abstract = True
        app_label = 'catalogue'
        ordering = ['-date_created']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def get_all_images(self):
        if self.is_child and not self.images.exists() and self.parent_id is not None:
            return self.parent.images.all()
        return self.images.all()
