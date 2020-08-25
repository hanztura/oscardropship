from .abstract_models import AbstractCategory


class Category(AbstractCategory):
    pass


from oscar.apps.catalogue.models import *  # noqa isort:skip
