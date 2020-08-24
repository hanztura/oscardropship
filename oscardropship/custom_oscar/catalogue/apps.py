import oscar.apps.catalogue.apps as apps

url = apps.url


class CatalogueConfig(apps.CatalogueConfig):
    name = 'oscardropship.custom_oscar.catalogue'

    def get_urls(self):
        urls = super(apps.OscarConfig, self).get_urls()
        urls += [
            url(r'^$', self.catalogue_view.as_view(), name='index'),
            url(
                r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
                self.detail_view.as_view(),
                name='detail'
            ),
            url(
                r'^collections/(?P<category_slug>[\w-]+(/[\w-]+)*)-(?P<pk>\d+)/$',
                self.category_view.as_view(),
                name='category'
            ),
            url(r'^ranges/(?P<slug>[\w-]+)/$',
                self.range_view.as_view(), name='range'),
        ]
        return self.post_process_urls(urls)
