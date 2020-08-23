from django.apps import AppConfig


def store_as_webp(sender, **kwargs):
    webp_path = sender.storage.path('.'.join([sender.name, 'webp']))
    sender.image.save(webp_path, 'webp')


class WagtailPagesConfig(AppConfig):
    name = 'wagtail_pages'

    def ready(self):
        super().ready()

        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(store_as_webp)
