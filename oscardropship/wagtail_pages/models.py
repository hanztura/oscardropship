from wagtail.core.models import Page


class HomePage(Page):
    def get_template(request, *args, **kwargs):
        return 'uikit/home.html'
