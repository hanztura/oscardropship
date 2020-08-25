from .abstract_models import AbstractCategory, AbstractProduct


class Category(AbstractCategory):
    pass


class Product(AbstractProduct):
    pass


from oscar.apps.catalogue.models import *  # noqa isort:skip
