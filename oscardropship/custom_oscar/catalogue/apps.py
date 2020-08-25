import oscar.apps.catalogue.apps as apps

from django.urls import path

url = apps.url


class CatalogueOnlyConfig(apps.CatalogueOnlyConfig):
    name = 'oscardropship.custom_oscar.catalogue'

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            url(r'^$', self.catalogue_view.as_view(), name='index'),
            url(
                r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                self.detail_view.as_view(),
                name='detail'
            ),
            path(
                'collections/<slug:category_slug>_<int:pk>/',
                self.category_view.as_view(),
                name='category'
            ),
            # url(
            #     r'^collections/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
            #     self.category_view.as_view(),
            #     name='category'
            # ),
            url(r'^ranges/(?P<slug>[\w-]+)/$',
                self.range_view.as_view(), name='range'),
        ]
        return self.post_process_urls(urls)


class CatalogueReviewsOnlyConfig(apps.CatalogueReviewsOnlyConfig):
    name = 'oscardropship.custom_oscar.catalogue'


class CatalogueConfig(CatalogueOnlyConfig, CatalogueReviewsOnlyConfig):
    pass
